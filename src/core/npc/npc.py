from ..entity import CustomEntity
import pygame as pg


class NPC(CustomEntity):

    def __init__(self,
                 name: str,
                 images: dict[str, list[pg.Surface]],
                 base_animation,
                 position: list[int]
                 ) -> None:

        super().__init__(
            name, images, base_animation, position
        )

        self.name = name
        self.position = position
        self.images = images
