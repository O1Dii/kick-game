from enum import Enum
from typing import Dict

import arcade

from base import SingltonMeta


class ViewTypes(Enum):
    StartMenu = 1
    About = 2
    Game = 3
    GameOver = 4


class ViewManager(metaclass=SingltonMeta):
    def __init__(self, window: arcade.Window, views: Dict[ViewTypes, arcade.View]) -> None:
        self.previous_view = None
        self.current_view = None
        self.window = window
        self.views = views

    def show_view(self, view_type: ViewTypes, *args, **kwargs):
        self.previous_view = self.window.current_view
        self.current_view = self.views[view_type](*args, **kwargs)
        self.window.show_view(self.current_view)

        if hasattr(self.current_view, 'setup'):
            self.current_view.setup()

    def show_previous_view(self):
        if self.previous_view is not None:
            self.current_view = self.previous_view
            self.window.show_view(self.current_view)
            self.previous_view = None
