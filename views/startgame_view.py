import arcade

from base.buttons import Button
from base.settings import Settings
from base.view_manager import ViewTypes


class MenuView(arcade.View):

    def __init__(self, view_manager):
        super().__init__()
        self.view_manager = view_manager
        self.button_list = []

        play_button = Button(Settings.WIDTH / 2, Settings.HEIGHT / 1.5, Settings.PLAY_BUTTON_TEXT,
                             lambda: self.view_manager.show_view(ViewTypes.Game))
        about_button = Button(Settings.WIDTH / 2, Settings.HEIGHT / 1.75, Settings.ABOUT_BUTTON_TEXT,
                              lambda: self.view_manager.show_view(ViewTypes.About))
        exit_button = Button(Settings.WIDTH / 2, Settings.HEIGHT / 2.1, Settings.EXIT_BUTTON_TEXT,
                             lambda: self.window.close())

        self.button_list.extend([play_button, about_button, exit_button])

    def on_show(self):
        arcade.set_background_color(Settings.MAIN_MENU_COLOR)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(Settings.GAME_NAME, Settings.WIDTH / 2, Settings.HEIGHT / 1.12,
                         Settings.MAIN_MENU_GAME_TITLE_COLOR, font_size=50, anchor_x='center')

        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        for button in self.button_list:
            if x > button.center_x + button.width / 2:
                continue
            if x < button.center_x - button.width / 2:
                continue
            if y > button.center_y + button.height / 2:
                continue
            if y < button.center_y - button.height / 2:
                continue
            button.on_press()

    def on_mouse_release(self, x, y, button, key_modifiers):
        for button in self.button_list:
            if button.pressed:
                button.on_release()
