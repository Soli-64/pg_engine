# Pg_Engine

pg_engine is a [pygame](https://github.com/pygame/pygame)-based library designed to create simple video-games using python. It includes scene system, 
GUI creation and theming thanks to [Pygame-GUI](https://github.com/MyreMylar/pygame_gui).

### Quick Start

Once in your virtualenv, run these commands:

````bash
pip install pygame==2.6.0 pygame-gui==0.6.9 pyscroll==2.31 pytmx==3.32
````

````bash
git submodule add -f https://github.com/Soli-64/pg_engine .\venv\Lib\site-packages\pg_engine\
````

````python title="main.py"

import pygame
pygame.init()
from pg_engine import GameCore, GUIScene, Button

game = GameCore(
    window_name='My Own Game',
    resizable=True,
    starting_screen_delay=2000,
    bg_color=(43, 45, 48)
)

game.configure(fps=60)


class Menu(GUIScene):

    def __init__(self):
        super().__init__('home', game)

    def on_update(self) -> None:
        print('scene')

    def render(self) -> []:
        return [
            Button(
                rect=[((self.game.vw - 100) / 2, (self.game.vh - 50) / 2), (100, 50)],
                obj_id="#btn",
                text='Play',
                func=lambda: print('Hello World !')
            )
        ]


game.create_scene('gui', Menu())
game.go('gui')

game.run()

````
To update pg_engine dependance, use this command:

````bash
git submodule update --remote --merge
````