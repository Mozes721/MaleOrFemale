import numpy as np
import cv2


def classify_image(model, image):
    img = adjust_image(image)
    img = cv2.resize(image, (50, 50))
    img = img.reshape(1, -1)
    img = img / 255.0
    prediction = model.predict(img)[0]
    if prediction < 0.5:
        gender = 'female'
    else:
        gender = 'male'
    return gender


def adjust_image(image):
    resized_image = cv2.resize(image, (50, 50)) 
    resized_image = np.asarray(resized_image) / 255.0
    return resized_image
