from keras.models import load_model
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import os

classes = {0: "mild ", 1: "moderate ", 2:"close to none ", 3:"very mild "}

model = load_model('alzeihmers.h5')

def predict(model):
    datagen = ImageDataGenerator(rescale=1./255)
    path=datagen.flow_from_directory(directory="buffer", target_size=(224,224))
    prediction = model.predict(path)
    index = np.argmax(prediction)
    predict = prediction[0][index]

    return (f"You have {classes[index]} chance of Alzheimers")

