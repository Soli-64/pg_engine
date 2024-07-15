<!DOCTYPE html>
<html>

<h1> Pygame2DEngine </h1>

<h2> 
    Pygame2DEngine is a pygame-based library made for create 2D Games, 
    including GUI thanks to the library PygameGUI. <br>
</h2>

<h3>
    It implements scene-system (with a special scene for Tiled maps using PyTmx),
    customizable player and NPC, easy GUI gestion with PygameGUI theming and dialogs.
</h3>

<h2> Quick Start </h2>

<code style="font-size: 1.2em">

    from pg_engine import GameCore, GUIScene, Button

    game = GameCore(
        window_name='My Own Game',
        window_icon='./assets/images/mc2.png',
        resizable=True,
        starting_screen_delay=2000,
        bg_color=(43, 45, 48)
    )

    game.configure(fps=60)


    class Menu(GUIScene):

        def __init__(self):
            super().__init__('home', game)

        def on_update() -> None:
            print('scene
    
        def render(self) -> []:
            return [
                Button(
                    rect=[((self.game.vw-100)/2, (self.game.vh-50)/2), (100, 50)],
                    obj_id="#btn",
                    text='Play',
                    func=lambda: print('Hello World !)
                )
            ]


    game.create_scene('gui', Menu())
    game.go('gui')

    game.run()

</code>

</html>

