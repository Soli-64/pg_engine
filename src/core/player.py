import pygame
import pygame as pg
from .entity import DefaultEntity


class DefaultPlayer(DefaultEntity):

    def __init__(self, images, game, map_manager=None, position=(100, 100)):
        self.x, self.y = position
        super().__init__("player", images, self.x, self.y)

        # Instances
        self.game = game
        self.map_manager = map_manager

        # Attributes
        self.reach = 15
        self.speed = 5
        self.level = 1
        self.max_health = 400
        self.health = 400
        self.damage = 10
        self.money = 0
        self.xp = 0

        self.on_long_press = {
            pygame.K_UP: lambda: self.move('up'),
            pygame.K_LEFT: lambda: self.move('left'),
            pygame.K_RIGHT: lambda: self.move('right'),
            pygame.K_DOWN: lambda: self.move('down'),
        }
        self.on_press = {
            pygame.K_RSHIFT: lambda: self.move(self.direction, 3),
            pygame.K_g: lambda: map_manager.check_npc_collision()
        }

        self.movable = True
        self.interact_wall = True

    def set_manager(self, map_manager):
        self.map_manager = map_manager

    def handle_press(self, event):
        if event.type == pg.KEYDOWN:
            for key in self.on_press.keys():
                if event.key == key:
                    self.on_press[key]()

    def handle_long_press(self):
        pressed = pygame.key.get_pressed()

        for key in self.on_long_press.keys():
            if self.movable:
                if pressed[key]:
                    self.on_long_press[key]()
                    return


class CustomPlayer(DefaultPlayer):

    def __init__(self, image_path, game, map_manager=None):
        super().__init__(image_path, game, map_manager)

        self.on_long_press = {
            pygame.K_UP: lambda: self.move('up'),
            pygame.K_LEFT: lambda: self.move('left'),
            pygame.K_RIGHT: lambda: self.move('right'),
            pygame.K_DOWN: lambda: self.move('down'),
        }
        self.on_press = {
            pygame.K_RSHIFT: lambda: self.move(self.direction, 3)
        }

    def add_on_press_event(self, key, func):
        """
        Add a instant event
        :param key:
        :param func:
        :return:
        """
        self.on_click[key] = func

    def on_collide(self, rects: list[pg.Rect]) -> None:
        """
        Called when the player collides one of the rect in param rects list
        :param rects:
        :return:
        """
        pass
