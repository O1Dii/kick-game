import os

import arcade
from base.settings import Settings
from base.view_manager import ViewManager, ViewTypes
from views.about_view import AboutView
from views.game_view import GameView
from views.gameover_view import GameOverView
from views.startgame_view import MenuView

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


def main():
    window = arcade.Window(Settings.WIDTH, Settings.HEIGHT, Settings.GAME_NAME)
    view_manager = ViewManager(window,
                               {
                                   ViewTypes.StartMenu: MenuView,
                                   ViewTypes.Game: GameView,
                                   ViewTypes.About: AboutView,
                                   ViewTypes.GameOver: GameOverView
                               })
    menu_view = MenuView(view_manager)
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
