import numpy as np
import os
from tensorflow.keras.models import load_model
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from classification.prediction_classifier import classify_image
import cv2

Builder.load_file('GUI/menu.kv')


class MyWidget(GridLayout):
    def __init__(self, model, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.model = model

    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print(f.read())

    def selected(self, filename):
        self.ids.image.source = filename[0]
        image_data = cv2.imread(filename[0], cv2.IMREAD_GRAYSCALE)
        classify_gender = classify_image(self.model, image_data)
        self.ids.classifierOutput.text = 'Prediction: ' + classify_gender
