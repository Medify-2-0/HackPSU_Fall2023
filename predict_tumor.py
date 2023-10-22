from keras.models import load_model
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

classes={0: "no", 1: "yes"}

model = load_model('tumor.h5')

image_path = 'external testing'

testing_datagen = ImageDataGenerator(rescale = 1./255,validation_split=0)

img = testing_datagen.flow_from_directory(directory = image_path, target_size=(224, 224))

prediction = (model.predict(img))
arr = np.array(model.predict(img))
index=np.argmax(model.predict(img))
predict=arr[0][index]

if index==0 and f"{100-predict*100:.2f}"=="100.00":
    print("Less than 1%", "chance of having tumor") 
elif index==0:   
    print(f"{100-predict*100:.2f}%", "of having tumor")
elif index==1 and f"{predict*100:.2f}"=="100.00":
    print("More than 99%", "chance of having tumor")
else:
    print(f"{predict*100:.2f}%", "of having tumor")

print(img)