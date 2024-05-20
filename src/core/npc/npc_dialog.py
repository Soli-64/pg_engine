import pygame as pg
from .npc import NPC


class DialogNPC(NPC):

    def __init__(self,
                 name: str,
                 images: dict[str, list[pg.Surface]],
                 base_animation: str,
                 position: list[int],
                 sentences: list[str]
                 ) -> None:

        super().__init__(
            name, images, base_animation, position
        )

        self.sentences = sentences

        self.index = 0
        self.max_index = len(self.sentences)-1

        self.current_sentence = self.sentences[self.index]

    def update_current_sentence(self):
        self.current_sentence = self.sentences[self.index]

    def next_dialog(self):

        if self.index + 1 >= len(self.sentences):
            self.index = 0
            return True

        else:
            self.index += 1
            self.update_current_sentence()
