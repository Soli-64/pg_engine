import sys

import pygame
import pygame as pg
import pygame_gui as pgui
from .scenes import TiledMapScene, PresentScene, GUIScene
from ..gui.element.dialog_box import DialogBox
from pygame.locals import *

pygame.init()


class GameCore:
    """
        The game core
    """

    def __init__(self,
                 window_name: str,
                 window_icon: str = '',
                 window_size: tuple[int, int] = max(pg.display.get_desktop_sizes()),
                 starting_screen_delay: int = 3000,
                 fullscreen=False,
                 resizable=True,
                 bg_color=(0, 0, 0)) -> None:

        # Config variables
        self.config = {}
        self.fps = 60
        self.bg_color = bg_color
        self.dialoging = False

        self.starting_screen_delay = starting_screen_delay

        # Window variables
        self.name = window_name
        self.resizable = resizable

        screen_size = window_size
        w, h = screen_size
        h -= 80
        screen_size = (w, h)
        self.dimensions = screen_size
        self.vw, self.vh = self.dimensions

        pg.display.set_caption(self.name, window_icon)

        self.screen = pg.display.set_mode(self.dimensions, RESIZABLE if self.resizable else 0)

        if fullscreen:
            pg.display.toggle_fullscreen()

        # Core variables
        self.running = False
        self.clock = None
        self.game_scenes = {}
        self.events_functions = {}
        self.current_scene = []

        self.maintained_events = {}
        self.pressed_events = {
            pg.K_SPACE: lambda: self.stop_dialog()
        }

        self.ui_manager = pgui.UIManager(self.screen.get_size())

        self.dialog_box = DialogBox(pg.rect.Rect((self.vw/8, self.vh/8*7), (self.vw/8*6, self.vh/8)),
                                    self.ui_manager,
                                    True,
                                    50)

    # --- CONFIG

    def configure(self,
                  fps: int = None,
                  pressed_events=None,
                  maintained_events=None,
                  bg_color: tuple[int, int, int] = None,
                  ) -> None:
        """
        Configure basic game information
        :param fps:
        :param bg_color:
        :param pressed_events:
        :param maintained_events:
        :return:
        """
        if fps is not None:
            self.fps = fps
        if bg_color is not None:
            self.bg_color = bg_color
        if pressed_events is not None:
            for key in pressed_events.keys():
                self.pressed_events[key] = pressed_events[key]
        if maintained_events is not None:
            for key in maintained_events.keys():
                self.maintained_events[key] = maintained_events[key]

    def add_pressed_event(self, key: int, event) -> None:
        self.pressed_events[key] = event

    def add_maintained_event(self, key: int, event) -> None:
        self.maintained_events[key] = event

    @staticmethod
    def toggle_fullscreen():
        pg.display.toggle_fullscreen()

    # --- DIALOG

    def new_dialog(self, text: str, progressive=True):
        """
        Create a Dialog Box
        :param text:
        :param progressive:
        :return:
        """
        self.dialog_box = DialogBox(pg.rect.Rect((self.vw / 5, self.vh / 8 * 6.75), (self.vw / 10 * 6, self.vh / 8)),
                                    self.ui_manager,
                                    progressive,
                                    30)
        self.dialoging = True
        self.dialog_box.set_text(text)

    def stop_dialog(self):
        """
        Stop the dialog and close the dialog_box
        :return:
        """
        if self.dialoging:
            self.dialog_box.close()
            self.dialoging = False

    # --- GUI FUNCTIONS

    def reset_gui(self) -> None:
        """
            Delete all ui elements on all scenes
        """
        self.ui_manager.clear_and_reset()

    # --- UI MANAGER FUNCTIONS

    def load_file_theme(self, file_path: str) -> None:
        """
        Load a pygame_gui theme from a jon file. \n
        For theming look at: https://pygame-gui.readthedocs.io/en/v_069/theme_guide.html
        :param file_path:
        :return:
        """
        self.ui_manager.get_theme().load_theme(file_path)

    def load_theme_dict(self, theme: dict) -> None:
        """
        Load a theme from a dict \n
        For theming look at: https://pygame-gui.readthedocs.io/en/v_069/theme_guide.html
        :param theme:
        :return:
        """
        self.ui_manager.ui_theme._parse_theme_data_from_json_dict(theme)

    # --- SCENE FUNCTIONS

    def create_scene(self, scene_name: str, game_scene: (PresentScene, GUIScene, TiledMapScene)):
        """
            Add a new Scene to your game
            :param scene_name: string
            :param game_scene: Instance of your Scene
        """
        game_scene.setup()
        self.game_scenes[scene_name] = game_scene

    def set_scene_visible(self, scene_name: str):
        """
            Set a scene visible thanks to his name
            :param scene_name: str
            :return:
        """
        s = self.game_scenes[scene_name]
        self.current_scene.append(s)
        self.resize_display_mode(self.vw, self.vh)

    def set_scene_hidden(self, scene_name: str):
        """
            Hid a scene thanks to his name
        :param scene_name: str
        :return:
        """
        s = self.game_scenes[scene_name]
        self.current_scene.remove(s)
        self.resize_display_mode(self.vw, self.vh)

    def go(self, scene_name: str):
        """
            Set one only scene visible
        :param scene_name:
        :return:
        """
        s = self.game_scenes[scene_name]
        self.current_scene = [s]
        self.resize_display_mode(self.vw, self.vh)

    # --- GAME CORE

    def resize_display_mode(self, vw: int, vh: int) -> None:
        """
        Resize the window, refresh the gui and scenes
        :param vw:
        :param vh:
        :return:
        """
        self.vw = vw
        self.vh = vh
        self.reset_gui()
        for s in self.current_scene:
            s.setup()

    def _handle_inputs(self):
        maintained = pg.key.get_pressed()
        for key in self.maintained_events.keys():
            if maintained[key]:
                self.maintained_events[key]()
                return

    def _handle_events(self, event):
        """
            Apply basic game events and customs added:
            - Quit
            - Resize
        :param event:
        :return:
        """

        self._handle_inputs()

        if event.type == pg.QUIT:
            self.running = False

        elif event.type == VIDEORESIZE:
            self.resize_display_mode(event.w, event.h)

        elif event.type == pg.KEYDOWN:

            for key in self.pressed_events.keys():
                if event.key == key:
                    self.pressed_events[key]()

    def stop(self):
        """
          - Stop the game loop
          - **Warning!** this function close the window and stop the programme
        """
        self.running = False
        pg.quit()
        sys.exit(0)

    def run(self):
        """
            Run the game
        :return:
        """
        self.clock = pg.time.Clock()
        self.running = True

        starting_scene = PresentScene(self)

        next_scene = self.current_scene

        self.create_scene('present', starting_scene)
        self.go('present')

        while self.running:

            if pg.time.get_ticks() <= self.starting_screen_delay:

                starting_scene.update()
                time_delta = self.clock.tick(self.fps) / 1000
                self.ui_manager.update(time_delta)
                self.ui_manager.draw_ui(self.screen)

                pg.display.flip()

                for event in pg.event.get():
                    self._handle_events(event)

            else:

                if starting_scene is not None:

                    starting_scene.remove_elements(['#use_strict_present_panel', '#use_strict_present_label'])

                    self.current_scene = next_scene
                    self.resize_display_mode(self.vw, self.vh)

                    starting_scene = None

                time_delta = self.clock.tick(self.fps) / 1000

                # Scenes update

                for s in self.current_scene:
                    s.update()

                # dialog managing

                if self.dialoging:

                    self.dialog_box.dialog_box.show()
                    self.dialog_box.update()
                else:

                    self.dialog_box.dialog_box.hide()

                # Events management
                for event in pg.event.get():

                    self._handle_events(event)

                    for s in self.current_scene:
                        s.handle_event(event)

                    self.ui_manager.process_events(event)

                    # Check EventButton pressed
                    if event.type == pgui.UI_BUTTON_START_PRESS:
                        button_id = event.ui_element.object_ids[len(event.ui_element.object_ids) - 1]
                        for game_btn_id in self.events_functions.keys():
                            if button_id == game_btn_id:
                                self.events_functions[game_btn_id]()
                                break

                    # Check entry submit
                    elif event.type == pg.USEREVENT and event.user_type == pgui.UI_TEXT_ENTRY_FINISHED:
                        entry_id = event.ui_element.object_ids[len(event.ui_element.object_ids) - 1]
                        for game_entries_id in self.events_functions.keys():
                            if entry_id == game_entries_id:
                                self.events_functions[entry_id](event.text)
                                break

                self.ui_manager.update(time_delta)
                self.ui_manager.draw_ui(self.screen)

                # Window update
                pg.display.flip()

                self.screen.fill(self.bg_color)

        pg.quit()
