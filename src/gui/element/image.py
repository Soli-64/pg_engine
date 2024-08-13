

class Image:

    def __init__(self,
                 rect: list[tuple[int, int], tuple[int, int]],
                 image_path: str,
                 obj_id: str,
                 class_id: str
                 ):
        self.rect = rect
        self.obj_id = obj_id
        self.class_id = class_id
        self.image_path = image_path
