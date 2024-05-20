import pygame_gui as pgui
import pygame as pg


class DialogBox:

    def __init__(self, rect: pg.Rect, ui_manager: pgui.UIManager, progressive_text=False, text_speed=0):
        self.rect = rect
        self.text = ''
        self.ui_manager = ui_manager

        self.progressive = progressive_text
        self.text_speed = text_speed
        self.next_char_time = 0

        self.current_text = ''

        self.dialog_box = pgui.elements.UITextBox(
            html_text='',
            relative_rect=self.rect,
            manager=self.ui_manager
        )

    def set_text(self, text):
        self.text = text
        self.current_text = ''

    def close(self):
        self.set_text('')
        self.dialog_box.visible = False

    def update(self):
        if self.progressive:
            if len(self.current_text) < len(self.text) and pg.time.get_ticks() > self.next_char_time:
                self.current_text += self.text[len(self.current_text)]
                self.next_char_time = pg.time.get_ticks() + self.text_speed
                self.dialog_box.html_text = self.current_text
                self.dialog_box.rebuild()
        else:
            self.dialog_box.html_text = self.text
            self.dialog_box.rebuild()
