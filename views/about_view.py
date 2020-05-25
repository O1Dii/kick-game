import arcade

from base.settings import Settings
from base.view_manager import ViewTypes, ViewManager


class AboutView(arcade.View):

    def __init__(self, *args):
        super().__init__()
        self.view_manager = ViewManager()

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(Settings.ABOUT_VIEW_TITLE_TEXT, Settings.WIDTH/2, Settings.HEIGHT/1.25,
                         arcade.color.BLACK, font_size=40, anchor_x='center')
        arcade.draw_text(Settings.ABOUT_VIEW_TEXT, Settings.WIDTH/2, Settings.HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x='center')
        arcade.draw_text(Settings.RETURN_TEXT, Settings.WIDTH/2, Settings.HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x='center')

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.view_manager.show_view(ViewTypes.StartMenu, self.view_manager)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ENTER or symbol == arcade.key.ESCAPE:
            self.view_manager.show_view(ViewTypes.StartMenu, self.view_manager)
