from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from play import play


Builder.load_file('ui/screens/select_game_screen.kv')


class SelectGameScreen(Screen):
    def __init__(self, **kwargs):
        super(SelectGameScreen, self).__init__(name=kwargs.get('name'))

    def play_callback(self):
        play()