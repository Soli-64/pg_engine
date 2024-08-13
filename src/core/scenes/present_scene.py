from .gui_scene import GUIScene
from .. import Panel, Image, Input, Label, Button
import pygame as pg


class PresentScene(GUIScene):

    def __init__(self, game):
        self.progbar_width = 0
        super().__init__('present', game, '')

        self.game.load_theme_dict(
            {

                "#use_strict_present_panel": {
                    "colours": {
                        "normal_bg": "#191919",
                        "dark_bg": "#191919"
                    }
                },

                "#use_strict_present_label": {
                    "colours": {
                        "normal_bg": "#191919",
                        "dark_bg": "#191919"
                    },
                    "font": {
                        "size": 45,
                        "bold": "900"
                    }
                },
                "#progbar1": {
                    "colours": {
                        "normal_bg": "#fff",
                        "dark_bg": "#fff"
                    }
                },
                "#progbar2": {
                    "colours": {
                        "normal_bg": "#000",
                        "dark_bg": "#000"
                    }
                },

                "@e": {},
            }
        )

    def update(self):
        self.progbar_width = (self.game.vw/6*4) * pg.time.get_ticks() / (self.game.starting_screen_delay - 500) - 500
        self.setup()

    def render(self) -> []:
        return [
            Panel(
                rect=[(0, 0), self.game.screen.get_size()],
                class_id='@e',
                obj_id="#use_strict_present_panel",
                children=[
                    Label(
                        rect=[((self.game.vw - 800) / 2, (self.game.vh - 400) / 2), (800, 400)],
                        text=" Powered by PygameEngine",
                        class_id='@e',
                        obj_id="#use_strict_present_label"
                    ),
                    Panel(
                        rect=[(self.game.vw/6, self.game.vh/8*6), (self.game.vw/6*4, 40)],
                        class_id='@e',
                        obj_id='#progbar1',
                        children=[]
                    ),
                    Panel(
                        rect=[
                            (self.game.vw / 6, self.game.vh / 8 * 6),
                            (self.progbar_width, 40)],
                        class_id='@e',
                        obj_id='#progbar2',
                        children=[]
                    )

                ]
            )
        ]
