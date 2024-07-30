import pygame as pg


class Image:

    @staticmethod
    def load(
            path: str,
            size: tuple[int, int]
    ) -> pg.Surface:
        """
        Load an image with from **path** with **size** resolution
        :param path:
        :param size:
        :return:
        """
        image = pg.Surface.convert_alpha(pg.image.load(path))
        image = pg.transform.scale(image, size)

        return image

    @staticmethod
    def image_to_sprite(image: pg.Surface) -> pg.sprite.Sprite:
        """
        Transform an **image** to a **sprite**
        :param image:
        :return:
        """
        return ImageSprite(image)

    @staticmethod
    def images_superposition(
            size: tuple[int, int],
            image1: pg.Surface,
            image2: pg.Surface,
            image1_pos=(0, 0),
            image2_pos=(0, 0)) -> pg.Surface:
        """
        Create an **image** with two others superposition
        :param size:
        :param image1:
        :param image2:
        :param image1_pos:
        :param image2_pos:
        :return:
        """
        final_image = pg.Surface(size, pg.SRCALPHA)

        final_image.blit(image1, image1_pos)
        final_image.blit(image2, image2_pos)

        return final_image

    @staticmethod
    def get_image(
            image_path: str,
            x: int,
            y: int,
            w=32,
            h=32
    ) -> pg.Surface:
        """
        Get an image from **image_path** on position **x, y** and size **w, h** (default 32x32)
        :param image_path:
        :param x:
        :param y:
        :param w:
        :param h:
        :return:
        """
        image = pg.Surface([32, 32], pg.SRCALPHA)
        _ = pg.Surface.convert_alpha(pg.image.load(image_path))
        image.blit(_, (0, 0), (x, y, w, h))

        return image

    @staticmethod
    def get_split_images(
            folder_path: str,
            animation_name: str,
            images_highest_index: int,
            images_resolution=(64, 64)
    ) -> list[pg.Surface]:
        """
        This function is made for use **multiples images of an animation in a same folder** named with the animation
        name ,exemple: \n
        In the walk folder, we have: \n
        walk0.png, walk1.png, walk2.png \n
        - **! The first image indic must be 0** (walk0.png for exemple)
        - **! Images are get on size 64x64 by default**

        :param folder_path:
        :param animation_name:
        :param images_highest_index:
        :param images_resolution:
        :return:
        """
        images = []

        for i in range(0, images_highest_index+1):

            image = Image.load(f'{folder_path}/{animation_name}{i}.png', images_resolution)
            surface = pg.Surface(images_resolution, pg.SRCALPHA)
            surface.blit(image, (0, 0))
            images.append(surface)

        return images

    @staticmethod
    def get_onefile_images(image_path: str, y: int, images_size=(32, 32)) -> list[pg.Surface]:
        """
        This function is made for extract images from a line of an image. \n
        It extracts 3 images of **size** resolution (default 32x32) \n
        Returns a list of images ( pg.Surface )
        :param image_path:
        :param y:
        :param images_size:
        :return:
        """
        images = []

        for i in range(0, 3):
            x = i * 32
            w, h = images_size

            image = Image.get_image(image_path, x, y, w, h)
            images.append(image)

        return images


class ImageSprite(pg.sprite.Sprite):
    def __init__(self, image) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def rotate(self, degree: int) -> None:
        self.image = pg.transform.rotozoom(self.image, degree, 1)

