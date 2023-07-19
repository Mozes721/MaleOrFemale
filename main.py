from GUI.kivy_gui import MyWidget
from kivy.app import App
import pickle


class GenderClassifierApp(App):
    def build(self):
        with open('classification/model.pickle', 'rb') as f:
            model = pickle.load(f)
        return MyWidget(model)


if __name__ == '__main__':
    GenderClassifierApp().run()
