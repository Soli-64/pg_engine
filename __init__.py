"""

    PygameEngine is a python module based on PyGame and PyGame_Gui developed by Lso.

"""


from .src.core.game import GameCore
from .src.core.player import DefaultPlayer, CustomPlayer
from .src.core.entity import DefaultEntity, CustomEntity
from .src.core.animation.animation import AnimateSprite  # , AnimateEffectSprite

from .src.core.scenes import *
from .src.gui.elements import *

__version__ = 0, 1
__author__ = 'lso'
__author_email__ = "soli64.games@gmail.com"
__description__ = "Pygame Engine is a module made for create simple 2d games with pg. It implements scene system," \
                  "simplification of pygame_gui module, dialog, npc system and lot of other features. "
