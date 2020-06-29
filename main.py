from time import time

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import NoTransition
from kivy.uix.screenmanager import ScreenManager

from ui.screens.menu_screen import MenuScreen
from ui.screens.train_screen import TrainScreen
from ui.screens.select_game_screen import SelectGameScreen

import cv2


class MainBox(FloatLayout):
    def __init__(self, **kwargs):
        super(MainBox, self).__init__()
        self.screens = AnchorLayout(anchor_x='center', anchor_y='center')
        self.content = ScreenManager()
        self.content.transition = NoTransition()

        # screens
        self.content.add_widget(MenuScreen(name="menu"))
        self.content.add_widget(TrainScreen(name="train"))
        self.content.add_widget(SelectGameScreen(name="select"))

        self.screens.add_widget(self.content)
        self.add_widget(self.screens)


class GameApp(App):
    accent_color = [255 / 255, 64 / 255, 129 / 255, 1]

    def build(self):
        return MainBox()


if __name__ == '__main__':
    GameApp().run()
    cv2.destroyAllWindows()