import random
import pygame
from .scene import GameScene


class ProceduralGenerationTile:

    def __init__(self,
                 name: str,
                 size: tuple[int, int],
                 image
                 ):
        """

        :param name:
        :param size:
        :param image:
        """
        self.name = name
        self.width, self.height = size
        self.image = image


class ProceduralGenerationScene(GameScene):

    def __init__(self,
                 name: str,
                 game,
                 map_size: tuple[int, int],
                 tile_size: tuple[int, int],
                 areas_repartition: dict[int, ProceduralGenerationTile],
                 map_layer: list[int] =[]
                 ):

        """
        :param name:
        :param game:
        :param map_size:
        :param tile_size:
        :param areas_repartition: A dict of areas with is presence percentage in key
        :param map_layer: An array with number for each type of tile
        """

        super().__init__(name, game)

        self.width, self.height = map_size

        temp = 0
        for _ in areas_repartition.keys():
            temp += _

        if temp != 100:
            raise ValueError(' Error on ProceduralGenerationScene: areas presence percentage totals must be 100')
