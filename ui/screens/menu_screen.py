from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file('ui/screens/menu_screen.kv')


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(name=kwargs.get('name'))