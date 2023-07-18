from GUI.kivy_gui import MyWidget
from tensorflow.keras.models import load_model
from kivy.app import App


class GenderClassifierApp(App):
    def build(self):
        model = 'model.pickle'
        return MyWidget(model)

if __name__ == '__main__':
    GenderClassifierApp().run()
