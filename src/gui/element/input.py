

class Input:

    def __init__(self, rect: list[tuple[int, int], tuple[int, int]], obj_id: str, submit_func):
        self.rect = rect
        self.obj_id = obj_id
        self.submit_func = submit_func
