import arcade

from base.settings import Settings
from base.view_manager import ViewTypes, ViewManager


class GameOverView(arcade.View):
    def __init__(self, *, winner_id, time_taken):
        super().__init__()

        self.view_manager = ViewManager()
        self.winner_id = winner_id
        self.time_taken = time_taken

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(Settings.WINNER_TEXT_PATTERN % self.winner_id, Settings.WIDTH/3.35, Settings.HEIGHT/1.45, arcade.color.WHITE, 54)
        time_taken_formatted = f'{round(self.time_taken, 2)} seconds'
        arcade.draw_text(Settings.GAME_OVER_TIME_TITLE_PATTERN % time_taken_formatted,
                         Settings.WIDTH/2,
                         Settings.HEIGHT/2,
                         arcade.color.GRAY,
                         font_size=25,
                         anchor_x='center')

        arcade.draw_text(Settings.RETURN_TEXT, Settings.WIDTH/2.5, Settings.HEIGHT/2.5, arcade.color.WHITE, 24)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.view_manager.show_view(ViewTypes.StartMenu, self.view_manager)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ENTER or symbol == arcade.key.ESCAPE:
            self.view_manager.show_view(ViewTypes.StartMenu, self.view_manager)
