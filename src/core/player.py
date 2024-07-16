import pygame
import pygame as pg
from .entity import DefaultEntity


class DefaultPlayer(DefaultEntity):

    def __init__(self, image_path, game, map_manager=None, position=(100, 100)):
        self.x, self.y = position
        super().__init__("player", image_path, self.x, self.y)

        # Instances
        self.game = game
        self.map_manager = map_manager

        # image
        self.image_path = image_path

        # Attributes
        self.reach = 15
        self.speed = 5
        self.level = 1
        self.max_health = 400
        self.health = 400
        self.damage = 10
        self.money = 0
        self.xp = 0
        self.pressed_actions = {
            pygame.K_UP: lambda: self.move('up'),
            pygame.K_LEFT: lambda: self.move('left'),
            pygame.K_RIGHT: lambda: self.move('right'),
            pygame.K_DOWN: lambda: self.move('down'),
        }
        self.instant_actions = {
            pygame.K_RSHIFT: lambda: self.move(self.direction, 3),
            pygame.K_g: lambda: map_manager.check_npc_collision()
        }
        self.movable = True
        self.interact_wall = True

    def set_manager(self, map_manager):
        self.map_manager = map_manager

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            for key in self.instant_actions.keys():
                if event.key == key:
                    self.instant_actions[key]()

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        for key in self.pressed_actions.keys():
            if self.movable:
                if pressed[key]:
                    self.pressed_actions[key]()
                    return


class CustomPlayer(DefaultPlayer):

    def __init__(self, image_path, game, map_manager=None):
        super().__init__(image_path, game, map_manager)

        self.pressed_actions = {
            pygame.K_UP: lambda: self.move('up'),
            pygame.K_LEFT: lambda: self.move('left'),
            pygame.K_RIGHT: lambda: self.move('right'),
            pygame.K_DOWN: lambda: self.move('down'),
        }
        self.instant_actions = {
            pygame.K_RSHIFT: lambda: self.move(self.direction, 3)
        }
