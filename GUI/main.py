import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import os

# Designate Our .kv design file 
Builder.load_file('menu.kv')

class MyWidget(GridLayout):
    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print(f.read())

    def selected(self, filename):
        self.ids.image.source = filename[0]
        print("selected: %s" % filename[0])




class GenderClassifierApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    GenderClassifierApp().run()

