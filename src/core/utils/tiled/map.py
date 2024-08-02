import pygame
import pyscroll
import pytmx
from .teleporter import Teleporter


class Map:

    def __init__(self, name, file_path, entities_layer, teleporters, entities, collision_property):
        """
        :param name: Map name
        :param file_path: Path to the tmx file
        :param entities_layer: Position of entities in different layouts
        :param collision_property: property in Tiled for collision
        """
        self.name = name
        self.file_path = file_path
        self.entities_layer = entities_layer

        tmx_data = pytmx.util_pygame.load_pygame(file_path)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.tmx_data = tmx_data
        self.map_data = map_data

        self.collision_property = collision_property

        self.elements = {
            'teleporters': teleporters,
            'entities': entities,
            'walls': []
        }

        self.player = None
        self.screen = None
        self.map_layer = None
        self.group = None

    def register(self, screen=None, player=None, teleporters=None, entities=None, zoom=2.0):
        """
        Register the map with all data

        - player state \n
        - teleporters \n
        - entities \n
        - zoom
        :param screen:
        :param player:
        :param teleporters:
        :param entities:
        :param zoom:
        :return:
        """
        if screen is not None:
            self.screen = screen
        if player is not None:
            self.player = player
        if teleporters is not None:
            self.elements['teleporters'] = teleporters
        if entities is not None:
            self.elements['entities'] = entities

        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = zoom

        for tp in self.elements['teleporters']:
            self.add_teleporter(tp)

        for obj in self.tmx_data.objects:
            if obj.properties.get(self.collision_property):
                self.elements['walls'].append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=self.entities_layer)

        for entity in self.elements['entities']:
            entity.tmx_data = self.tmx_data
            entity.register()
            self.group.add(entity)

        if self.player is not None:
            self.group.add(self.player)

    def get_group(self): return self.group

    def add_teleporter(self, teleporter: Teleporter):
        if isinstance(teleporter, Teleporter):
            self.elements['teleporters'].append(teleporter)
        else:
            raise ' add_teleporter function argument must be Teleporter instance '

    def update(self):
        self.register(self.map_layer, self.player)

    def on_update(self):
        if self.player is not None:
            self.group.center(self.player.rect.center)
            self.group.update()
