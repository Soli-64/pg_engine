import pygame as pg


class GameScene:
    """
       The base GameScene class.
       You should not use it.
    """

    def __init__(self, name: str, game=None) -> None:
        self.name = name
        self.game = game
        self.musics = []
        self.pressed_keys = {}
        self.maintained_keys = {}

    def handle_customevents(self, event):

        maintained = pg.key.get_pressed()

        for key, func in enumerate(self.maintained_keys):
            if maintained[key]:
                return func()

        for key, func in enumerate(self.pressed_keys):
            if event.key == key:
                return func()

    def add_event(self, key: int, function, maintained=False):
        """
        Add an event to this scene \n
        Set maintained to True for a continue action while the type is down
        :param key:
        :param function:
        :param maintained:
        :return:
        """
        if maintained:
            self.maintained_keys[key] = function
        else:
            self.pressed_keys[key] = function

    def set_musics(self, musics):
        """
        **musics**:
            - **idle**: path of the default scene music
            - *You can add other keys with this patern*
                - **music_name**: [file_path, event_start, event_end]
        :param musics:
        :return: None
        """
        for key, value in enumerate(musics):
            if key == 'idle':
                self.add_new_music({
                    'name': 'idle',

                })

    def add_new_music(self, music):
        self.musics.append(music)

    def setup(self):
        pass

    def preload_visible(self):
        pass

    def resize(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    # --- USER USAGE

    def on_update(self):
        """
        Modify this function for execute your code while running the game
        :return:
        """
        pass
