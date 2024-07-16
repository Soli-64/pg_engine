import pygame
from .map import Map
from .. import DialogNPC, MovableNPC


class MapManager:

    def __init__(self, game, player):
        self.game = game
        self.maps = dict()
        self.current_map = None
        self.screen = game.screen
        self.player = player
        self.obstacle_property = 'obstacle'

    def set_player(self, player):
        self.player = player

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def check_npc_collision(self):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is DialogNPC:
                if self.game.dialoging:
                    finished = sprite.next_dialog()
                    if finished:
                        self.game.stop_dialog()
                    else:
                        self.game.new_dialog(sprite.current_sentence)
                else:
                    self.game.new_dialog(sprite.current_sentence)

    def check_collision(self):

        if self.player is not None:
            for portal in self.get_map().elements['teleporters']:
                if portal.from_world == self.current_map:
                    point = self.get_object(portal.origin_point)
                    rect = pygame.Rect(point.x, point.y, point.width, point.height)
                    if self.player.feet.colliderect(rect):
                        copy_portal = portal
                        self.current_map = portal.target_world
                        self.teleport_player(copy_portal.teleport_point)

        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def get_map(self):

        try:
            return self.maps[self.current_map]

        except Exception:
            raise ValueError('You must select a map before set the TiledMapScene visible')

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().elements['walls']

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def register_map(self, map: Map):

        self.maps[map.name] = map

    def update(self):
        self.get_group().update()
        self.check_collision()
        for npc in self.get_map().elements['entities']:
            if isinstance(npc, MovableNPC):
                npc.move()
