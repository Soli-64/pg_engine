

class Panel:

    def __init__(self,
                 rect: list[tuple[int, int], tuple[int, int]],
                 obj_id: str,
                 class_id: str,
                 children: list
                 ) -> None:

        self.rect = rect
        self.obj_id = obj_id
        self.class_id = class_id
        self.children = children
