from GUI.kivy_gui import MyWidget
from kivy.app import App

class GenderClassifierApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    GenderClassifierApp().run()