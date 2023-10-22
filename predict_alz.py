from keras.models import load_model
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import os

classes = {0: "no", 1: "yes"}

model = load_model('alzeihmers.h5')

def predict(model):
    datagen = ImageDataGenerator(rescale=1./255)
    path=datagen.flow_from_directory(directory="buffer", target_size=(224,224))
    prediction = model.predict(path)
    index = np.argmax(prediction)
    predict = prediction[0][index]

    if index == 0 and f"{100 - predict * 100:.2f}" == "100.00":
        return "Less than 1%", "chance of having a Alzheimers"
    elif index == 0:
        return f"{100 - predict * 100:.2f}%", "of having a Alzheimers"
    elif index == 1 and f"{predict * 100:.2f}" == "100.00":
        return "More than 99%", "chance of having a Alzheimers"
    else:
        return f"{predict * 100:.2f}%", "of having a Alzheimers"

