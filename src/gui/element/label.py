from typing import Callable


class Label:

    def __init__(self,
                 rect: list[tuple[int, int], tuple[int, int]],
                 text: str,
                 obj_id: str,
                 class_id: str
                 ) -> None:

        self.rect = rect
        self.text = text
        self.obj_id = obj_id
        self.class_id = class_id
