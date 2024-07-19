import pygame as pg


class AnimateSprite(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.animation_index = 0
        self.clock = 0

        self.image = None
        self.images: dict[str, list[pg.Surface]] = {}

        self.speed = 3

    def animations(self, name):
        self.image = self.images[name][self.animation_index]
        #self.image.set_alpha(0)
        #self.image.convert_alpha()
        self.clock += self.speed * 8

        if self.clock >= 170:

            self.animation_index += 1

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0


"""
class AnimateEffectSprite(pygame_engine.sprite.Sprite):

    def __init__(self, file_path, animation_name, images_number, position):
        super().__init__()
        self.file_path = file_path
        self.animation_name = animation_name
        self.images_number = images_number
        self.map_manager = None
        self.animation_index = 0
        self.position = [position[0] + 30, position[1] + 15]
        self.clock = 0
        self.speed = 3
        self.index = 0
        self.image = util.PygameImage.load_image('./assets/images/empty.png', (16, 16))

        self.set_none_image()

        self.rect = self.image.get_rect()
        self.images = self.get_split_images()

    def set_none_image(self):
        self.image = util.PygameImage.load_image('./assets/images/empty.png', (16, 16))

    def play_animation(self, map_manager, position):

        self.map_manager = map_manager
        self.position = position
        self.index = 0
        self.images_number = len(self.images)

        if self.map_manager.player.direction == 'up':
            self.rotate(90)
            self.rect.x = self.map_manager.player.rect.x + 7
            self.rect.y = self.map_manager.player.rect.y - 20
        elif self.map_manager.player.direction == 'right':
            self.rect.x = self.map_manager.player.rect.x + 25
            self.rect.y = self.map_manager.player.rect.y + 15
        elif self.map_manager.player.direction == 'left':
            self.rotate(180)
            self.rect.x = self.map_manager.player.rect.x - 13
            self.rect.y = self.map_manager.player.rect.y + 15
        elif self.map_manager.player.direction == 'down':
            self.rotate(270)
            self.rect.x = self.map_manager.player.rect.x + 5
            self.rect.y = self.map_manager.player.rect.y + 33
        else:
            print('Error on player direction')

    def stop_animation(self):
        self.set_none_image()

    def updated(self):
        self.rect.topleft = self.position
        self.image = self.images[self.animation_index]
        if self.map_manager.player.direction == 'up':
            self.rotate(90)
            self.rect.x = self.map_manager.player.rect.x + 7
            self.rect.y = self.map_manager.player.rect.y - 20
        elif self.map_manager.player.direction == 'right':
            self.rotate(0)
            self.rect.x = self.map_manager.player.rect.x + 25
            self.rect.y = self.map_manager.player.rect.y + 15
        elif self.map_manager.player.direction == 'left':
            self.rotate(180)
            self.rect.x = self.map_manager.player.rect.x - 13
            self.rect.y = self.map_manager.player.rect.y + 15
        elif self.map_manager.player.direction == 'down':
            self.rotate(270)
            self.rect.x = self.map_manager.player.rect.x + 5
            self.rect.y = self.map_manager.player.rect.y + 33
        self.animation_index += 1
        if self.animation_index >= self.images_number:
            self.animation_index = 0
            self.stop_animation()

    def rotate(self, degree):
        self.image = pygame_engine.transform.rotozoom(self.image, degree, 1)

    def get_split_images(self):
        images = []
        for i in range(0, self.images_number):
            image = util.PygameImage.load_image(f'{self.file_path}/{self.animation_name}{i}.png', (16, 16))
            images.append(image)
        return images
"""