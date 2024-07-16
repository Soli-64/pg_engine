from .scene import GameScene
from .. import transform_element


class GUIScene(GameScene):

    def __init__(self, name: str, game, file_theme_path: str = ''):
        super().__init__(name, game)
        self.elements = []
        self.ui_elements = []
        self.file_theme_path = file_theme_path
        self.draw()

    def render(self) -> []:
        return []

    def draw(self):
        self.elements = []
        self.add_elements(self.render())

    def add_elements(self, elements: list):
        """
            Add elements to this scene
        :param elements:
        :return:
        """
        for e in elements:
            self.elements.append(e)
        self.setup_gui()

    def remove_elements(self, obj_ids: list[str]) -> None:
        """
             Remove elements from them object_id
        :param obj_ids:
        :returns:
        """
        for _id in obj_ids:
            for e in self.ui_elements:
                if e.get_object_ids()[-1] == _id:
                    e.kill()

    def setup(self):
        """
            Init the gui
        :return:
        """
        self.ui_elements = []
        self.draw()

    def setup_gui(self, elements=None, element_p=None):
        element_parent = element_p
        if elements is None:
            modifying_elements = self.elements
        else:
            modifying_elements = elements
        for element in modifying_elements:
            result = transform_element(element, self.game, element_parent)
            if isinstance(result, list):
                self.setup_gui(result[1], result[0])
                self.ui_elements.append(result[0])
            else:
                self.ui_elements.append(result)

    def handle_event(self, event):

        self.handle_customevents(event)
