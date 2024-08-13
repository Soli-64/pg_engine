from typing import Callable


class Input:

    def __init__(self,
                 rect: list[tuple[int, int], tuple[int, int]],
                 obj_id: str,
                 class_id: str,
                 submit_func: Callable
                 ) -> None:

        self.rect = rect
        self.obj_id = obj_id
        self.class_id = class_id
        self.submit_func = submit_func
