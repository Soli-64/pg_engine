from .npc import NPC
import pygame as pg


class MovableNPC(NPC):

    def __init__(self,
                 name: str,
                 images,
                 base_animation: str,
                 speed: int = 3,
                 path_points: list[pg.Rect] = []
                 ) -> None:

        super().__init__(
            name, images, base_animation, [100, 100]
        )

        self.speed = speed
        self.current_point = 0

        self.points = path_points

        self.tmx_data = None
        self.object_name = None
        self.index_start = None
        self.nb_points = None

    def _move(self, direction, speed_boost=1):

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

    def move(self):

        if len(self.points) < 1:

            raise ValueError('You must select points for this NPC. \n'
                             'You can use the load_points_from_map methode or put points manually when'
                             'you create this MovableNPC instance')

        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point > self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self._move('down')

        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self._move('up')

        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self._move('left')

        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self._move('right')

        if self.rect.colliderect(target_rect):
            self.current_point = target_point

    def register(self):
        for num in range(self.index_start, self.nb_points+1):
            point = self.tmx_data.get_object_by_name(f"{self.object_name}{num}")
            point = pg.Rect(point.x, point.y, point.width, point.height)
            self.points.append(point)
        self.teleport_spawn()

    def load_points_from_map(self, object_name, index_start, index_end):
        """
        Load your **NPC points** from **the map**: \n
        exemple for points NPC1_0, NPC1_1, NPC1_2, NPC1_3
        :param object_name: the map_object name without index (here NPC1_ )
        :param index_start: the first point index (here 0)
        :param index_end: last point index
        :return:
        """

        if self.tmx_data is not None:
            raise ValueError(' You must load points before register this NPC in a Map ')

        self.object_name = object_name
        self.index_start = index_start
        self.nb_points = index_end

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()
