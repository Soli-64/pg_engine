import pygame
import pygame as pg
from .entity import DefaultEntity


class Player(DefaultEntity):

    def __init__(self, images, game, position=(100, 100), map_manager=None):
        self.x, self.y = position
        super().__init__("player", images, self.x, self.y)

        # Instances
        self.game = game
        if map_manager is not None:
            self.map_manager = map_manager
            self.map_manager.set_player(self)

        self.speed = 5

        self.on_long_press = {}
        self.on_press = {}

        self.collide_events = []

    def init_default_config(self) -> None:
        """
        Init default player moves with z, q, s, d keys
         :return:
        """

        self.add_on_long_press_event(pygame.K_z, lambda: self.move('up'))
        self.add_on_long_press_event(pygame.K_q, lambda: self.move('left'))
        self.add_on_long_press_event(pygame.K_d, lambda: self.move('right'))
        self.add_on_long_press_event(pygame.K_s, lambda: self.move('down'))

    def add_on_press_event(self, key, func):
        """
        Add an instant event
        :param key:
        :param func:
        :return:
        """
        self.on_press[key] = func

    def add_on_long_press_event(self, key, func):
        """
        Add an instant event
        :param key:
        :param func:
        :return:
        """
        self.on_long_press[key] = func

    def add_collide_event(self, rects: list[pg.Rect], function) -> None:
        """
        Param function is called when the player collides one of the rect in param rects list
        :param rects:
        :param function:
        :return:
        """
        self.collide_events.append((rects, function))

    def check_collide(self):

        for _ in self.collide_events:
            rects, function = _
            for rect in rects:
                if self.rect.colliderect(rect):
                    return function()

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
            if pressed[key]:
                self.on_long_press[key]()
                return
