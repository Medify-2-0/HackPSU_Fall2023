from keras.models import load_model
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import os

classes = {0: "no", 1: "yes"}

model = load_model('tumor.h5')

def predict(model):
    datagen = ImageDataGenerator(rescale=1./255)
    path=datagen.flow_from_directory(directory="buffer", target_size=(224,224))
    prediction = model.predict(path)
    index = np.argmax(prediction)
    predict = prediction[0][index]

    if index == 0 and f"{100 - predict * 100:.2f}" == "100.00":
        return "Less than 1%", "chance of having a tumor"
    elif index == 0:
        return f"{100 - predict * 100:.2f}%", "of having a tumor"
    elif index == 1 and f"{predict * 100:.2f}" == "100.00":
        return "More than 99%", "chance of having a tumor"
    else:
        return f"{predict * 100:.2f}%", "of having a tumor"

'''average_prediction = np.mean(total_predictions, axis=0)
index = np.argmax(average_prediction)
predict = average_prediction[0][index]

if index == 0 and f"{100 - predict * 100:.2f}" == "100.00":
    print("Less than 1%", "chance of having a tumor")
elif index == 0:
    print(f"{100 - predict * 100:.2f}%", "of having a tumor")
elif index == 1 and f"{predict * 100:.2f}" == "100.00":
    print("More than 99%", "chance of having a tumor")
else:
    print(f"{predict * 100:.2f}%", "of having a tumor")'''
