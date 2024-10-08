# import pg as pg
from ..utils.tiled.map_manager import MapManager
from ..utils.tiled.map import Map
from ..player import Player
from .gui_scene import GUIScene


class TiledMapScene(GUIScene):
    """
    The TiledMapScene is made for create a 2D game using tiled maps \n
    It's one of the easiest way to create a game with tiled maps, but it's limited. \n
    """

    def __init__(self,
                 name: str,
                 game=None,
                 map_zoom=2,
                 file_theme_path: str = ""
                 ) -> None:
        super().__init__(name=name, game=game, file_theme_path=file_theme_path)

        self.player = None

        self.map_manager = MapManager(self.game, self.player)
        self.map_zoom = map_zoom

    def set_player(self, player):
        self.player = player
        self.player.set_manager(self.map_manager)

    # --- MAP

    def set_map_zoom(self, zoom: float) -> None:
        """
        Modify the map zoom (default is 2)
        :param zoom:
        :return:
        """
        self.map_zoom = zoom
        self.map_manager.maps[self.map_manager.current_map].register(zoom=self.map_zoom)

    def add_map(self, _map: Map) -> None:
        """
        Add a new map to this scene
        :param _map:
        :return:
        """
        if self.player is None:
            raise ValueError('\nYou must select a player for this scene before create a map.'
                             '\nYou can do TiledMapScene.use_default_player() for a simple player without configuration'
                             '\nor TiledMapScene.configure_player( CustomPlayer(...) ) for an advanced player. ')
        else:
            _map.register(self.game.screen, self.player, zoom=self.map_zoom)
            self.map_manager.register_map(_map)

    def select_map(self, map_name: str) -> None:
        """
        select the current map
        :param map_name: the map name
        :return:
        """
        self.map_manager.current_map = map_name
        self.player.add_collide_event(self.map_manager.get_walls(), self.player.move_back)

    # --- ENTITIES

    # --- PLAYER

    def teleport_player(self, teleport_point: str):
        """
        Change the player's position
        :param teleport_point: name of the teleport point
        :return:
        """

        point = self.map_manager.get_object(teleport_point)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def configure_player(self, player: Player) -> None:
        self.player = player
        self.map_manager.set_player(self.player)

    # --- EVENT / UPDATE

    def handle_event(self, event) -> None:
        """
        Apply scene events and custom events you can have added.
        :param event:
        :return:
        """

        if self.player is not None:
            self.player.handle_press(event)

    def update(self) -> None:

        if self.player is not None:
            self.player.save_location()
            self.player.handle_long_press()

        self.map_manager.update()
        self.map_manager.draw()

        self.on_update()
