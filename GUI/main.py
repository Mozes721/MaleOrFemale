import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<MyWidget>:
    id: my_widget
    FileChooserIconView:
        id: filechooser
        on_selection: my_widget.selected(filechooser.selection)
    Image:
        id: image
        source: ""
""")

class MyWidget(BoxLayout):
    
    def selected(self,filename):
        try:
            self.ids.image.source = filename[0]
        except:
            pass



class GenderClassifierApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    GenderClassifierApp().run()

