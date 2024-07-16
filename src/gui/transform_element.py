from .elements import Panel, Input, Label, Button, Image
from pygame_gui.elements import UIButton, UIPanel, UILabel, UITextEntryLine, UIImage
import pygame as pg
from pygame_gui.core import ObjectID


def transform_element(element, game, container=None):
    if isinstance(element, Label):
        return UILabel(
            relative_rect=pg.Rect(element.rect),
            text=element.text,
            manager=game.ui_manager,
            container=container,
            object_id=ObjectID(object_id=element.obj_id, class_id='@e')
        )

    elif isinstance(element, Panel):
        return [UIPanel(
            relative_rect=pg.Rect(element.rect),
            manager=game.ui_manager,
            container=container,
            object_id=ObjectID(object_id=element.obj_id[0], class_id='@e')
        ), element.children]

    elif isinstance(element, Button):
        game.events_functions[element.obj_id[0]] = element.func
        return UIButton(
            relative_rect=pg.Rect(element.rect),
            text=element.text,
            manager=game.ui_manager,
            container=container,
            object_id=ObjectID(class_id='@e', object_id=element.obj_id[0])
        )

    elif isinstance(element, Input):
        game.events_functions[element.obj_id[0]] = element.submit_func
        return UITextEntryLine(
            relative_rect=pg.Rect(element.rect),
            manager=game.ui_manager,
            container=container,
            object_id=ObjectID(class_id='@e', object_id=element.obj_id[0])
        )

    elif isinstance(element, Image):
        return UIImage(
            relative_rect=pg.Rect(element.rect),
            manager=game.ui_manager,
            container=container,
            object_id=ObjectID(class_id='@e', object_id=element.obj_id),
            image_surface=pg.image.load(element.image_path)
        )

    else:

        return UILabel(
            relative_rect=pg.Rect([(100, 100), (100, 100)]),
            text='Error while transforming this element',
            manager=game.ui_manager,
            container=None
        )
