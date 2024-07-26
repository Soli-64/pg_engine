import pygame
pygame.init()
from src.core.game import GameCore
from src.core.scenes.gui_scene import GUIScene
from src.core.scenes.tiled_map_scene import TiledMapScene
from src.gui.elements import *
from src.core.utils.tiled import *
from src.core.npc import MovableNPC, DialogNPC
from src.core.utils.image import Image
from src.core.player import Player


game = GameCore(
    window_name='My Own Game',
    window_icon='./assets/images/mc2.png',
    resizable=True,
    starting_screen_delay=2000,
    bg_color=(43, 45, 48)
)

game.configure(fps=60)


class MapScene(TiledMapScene):

    def __init__(self):
        super().__init__('map', game=game, map_zoom=4)

        player_image_path = './assets/images/sprite/default_player.png'
        self.set_player(Player(
            images={
                'down': Image.get_onefile_images('./assets/images/sprite/default_player.png', 0),
                'left': Image.get_onefile_images('./assets/images/sprite/default_player.png', 32),
                'right': Image.get_onefile_images('./assets/images/sprite/default_player.png', 64),
                'up': Image.get_onefile_images('./assets/images/sprite/default_player.png', 96),
            },
            game=self.game,
            map_manager=self.map_manager,
            position=(200, 200)
        ))

        self.player.init_default_config()

        npc = MovableNPC(
            name='bob',
            images={
                'down': Image.get_onefile_images('./assets/images/sprite/default_player.png', 0),
                'left': Image.get_onefile_images('./assets/images/sprite/default_player.png', 32),
                'right': Image.get_onefile_images('./assets/images/sprite/default_player.png', 64),
                'up': Image.get_onefile_images('./assets/images/sprite/default_player.png', 96),
            },
            base_animation='down',
            speed=2
        )
        npc.load_points_from_map('NPC1_', 0, 3)

        self.add_map(
            Map(
                name='carte',
                file_path='./assets/map/carte.tmx',
                entities_layer=0,
                teleporters=[],
                entities=[
                    npc,
                    DialogNPC('robin', {
                                'down': Image.get_onefile_images('./assets/images/sprite/default_player.png', 0),
                                'left': Image.get_onefile_images('./assets/images/sprite/default_player.png', 32),
                                'right': Image.get_onefile_images('./assets/images/sprite/default_player.png', 64),
                                'up': Image.get_onefile_images('./assets/images/sprite/default_player.png', 96)},
                              'down', [100, 100], ['Salut, ça va ?', 'Comment t"appelles tu ?']
                              )
                ],
                collision_property='obstacle'
            )
        )

        self.select_map('carte')

        self.player.add_collide_event(self.map_manager.get_objects_rects_by_property('collision'), lambda: print('test'))

    def on_update(self) -> None:
        self.apply_force([(self.player, lambda: not self.player.check_collide())], 'N', 3)

    def render(self) -> list:
        return [
            Panel(
                rect=[(20, 20), (300, (self.game.vh - 40))],
                obj_id='#panel',
                children=[
                    Label(
                        rect=[(10, 20), (260, 40)],
                        text="Player Name",
                        obj_id="#"
                    ),
                    Button(
                        rect=[(10, 80), (260, 40)],
                        text="Menu",
                        func=lambda: menu(),
                        obj_id='#menu_btn'
                    ),
                    Button(
                        rect=[(10, 140), (260, 40)],
                        text="full_screen",
                        func=lambda: self.game.toggle_fullscreen(),
                        obj_id='#fullscreen_btn'
                    )
                ]
            )
        ]


class Menu(GUIScene):

    def __init__(self):
        super().__init__('home', game)

    def render(self) -> []:
        return [
            Button(
                rect=[((self.game.vw-100)/2, (self.game.vh-50)/2), (100, 50)],
                obj_id="#btn",
                text='Play',
                func=lambda: mapper()
            )
        ]


game.create_scene('gui', Menu())
game.create_scene('map', MapScene())


def menu(): game.go('gui')


def mapper(): game.go('map')


menu()

game.run()
