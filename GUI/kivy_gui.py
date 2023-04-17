import kivy
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import cv2
from tensorflow.keras.models import load_model
import os
from classification.prediction_classifier import classify_image

# Designate Our .kv design file 
Builder.load_file('GUI/menu.kv')

class MyWidget(GridLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.model = load_model('classification/model.pickle')

    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print(f.read())

    def selected(self, filename):
        self.ids.image.source = filename[0]
        classify_gender = classify_image(self.model, filename[0])
        self.ids.label.text = 'Prediction: ' + classify_gender



