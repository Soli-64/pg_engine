import pygame as pg
from .utils.image import Image
from .animation.animation import AnimateSprite


class DefaultEntity(AnimateSprite):
    """
    The class for default Game Entities

    - **Advertisement** All images are extract on 32x32 on a single file, with format file give in documentation.
    For other use you should use a CustomEntity instance
    """

    def __init__(self, name: str, image_path, x: int, y: int):
        super().__init__()

        self.image_path = image_path
        self.images = {
            'down': Image.get_onefile_images(self.image_path, 0),
            'left': Image.get_onefile_images(self.image_path, 32),
            'right': Image.get_onefile_images(self.image_path, 64),
            'up': Image.get_onefile_images(self.image_path, 96),
        }
        self.name = name
        self.type = 'entity'

        self.direction = 'down'

        self.sprite_sheet = Image.load(self.image_path, (32, 32))

        self.animations('down')
        """self.image = Image.get_image(self.image_path, 0, 0)
        self.image.set_colorkey(0, 0)"""

        self.rect = self.image.get_rect()
        self.feet = pg.Rect(0, 0, self.rect.width * 0.5, 12)

        self.position = [x, y]
        self.old_position = self.position.copy()

        self.speed = 3

    def save_location(self):
        self.old_position = self.position.copy()

    def move(self, direction, speed_boost=1):

        self.animations(direction)
        self.direction = direction

        for x in range(speed_boost):
            if direction == 'up':
                self.position[1] -= self.speed
            elif direction == 'left':
                self.position[0] -= self.speed
            elif direction == 'right':
                self.position[0] += self.speed
            elif direction == 'down':
                self.position[1] += self.speed

    def dash(self):
        self.save_location()
        self.move(self.direction, 2)

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position

    def register(self): pass


class CustomEntity(AnimateSprite):
    """
    A customizable entity
    """

    def __init__(self,
                 name: str,
                 images: dict[str, list[pg.Surface]],
                 base_animation: str = 'idle',
                 position=(100, 100)

                 ) -> None:
        """
        **Advertisement** \n
        **images param must be a dict on this format:** \n
        { 'animation-name': [list of images] } \n
        exemple: \n
        { 'walk': Image.get_split_images('./images/sprite/player/walk', 'walk', 6) } \n
        or \n
        { 'walk': [Image.load('walk0.png'),Image.load('walk1.png'),Image.load('walk2.png')]

        :param name:
        :param images:
        :param position:
        """
        super().__init__()

        self.type = 'entity'

        self.position = position
        self.old_position = self.position #.copy()
        self.x, self.y = self.position

        self.name = name

        self.images = images
        self.animations(base_animation)

        self.rect = self.image.get_rect()
        self.feet = pg.Rect(0, 0, self.rect.width * 0.5, 12)

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def save_location(self):
        self.old_position = self.position.copy()

    def move_back(self):
        self.position = self.old_position

    def on_update(self):
        pass

    def register(self): pass
