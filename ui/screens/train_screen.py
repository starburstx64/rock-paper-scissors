from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from gather_images import gather_images
from train import train_and_save_model

Builder.load_file('ui/screens/train_screen.kv')


class TrainScreen(Screen):
    def __init__(self, **kwargs):
        super(TrainScreen, self).__init__(name=kwargs.get('name'))

    def gather_images_callback(self, type_spinner, num_samples_spinner, train_button):
        gather_images(type_spinner.text, int(num_samples_spinner.text), (True, False)[train_button.state == 'down'])

    def train_model(self, learning_rate_spinner, epochs_spinner):
        acc = train_and_save_model(float(learning_rate_spinner.text), int(epochs_spinner.text))

        popup = Popup(title='Model accuracy',
                      content=Label(text=str(acc)),
                      size_hint=(None, None), size=(200, 100))
        popup.open()

