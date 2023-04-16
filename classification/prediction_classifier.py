import numpy as np
import cv2

def sigmoid(z):
    y_head = 1/(1+np.exp(-z))
    return y_head

def classify_image(modal, filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (50, 50))
    img = img.reshape(1, 50, 50, 1)
    img = img / 255.0
    prediction = modal.predict(img)[0][0]
    if prediction < 0.5:
        gender = 'female'
    else:
        gender = 'male'
    return gender
  