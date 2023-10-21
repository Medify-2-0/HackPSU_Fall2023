from numpy import resize
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.applications import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D, Activation

data_gen=ImageDataGenerator(rescale=1./255, horizontal_flip=True)

train= data_gen.flow_from_directory(
    directory= "training",
    target_size=(224,224),
    shuffle=True,
    batch_size=64
)

valid=data_gen.flow_from_directory(
    directory= "validating",
    target_size=(224,224),
    batch_size=64
)

test=data_gen.flow_from_directory(
    directory= "testing",
    target_size=(224,224),
    batch_size=64
)


model = Sequential()
model.add(Conv2D(32, (3,3), input_shape = (224,224,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(32, (3,3), input_shape = (224,224,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(64, (3,3), input_shape = (224,224,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(64, (3,3), input_shape = (224,224,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(2, activation="sigmoid"))
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])
    
early_stopping = keras.callbacks.EarlyStopping(
    patience=10,
    min_delta=0.001,
    restore_best_weights=True)

history = model.fit(
    train,
    validation_data= valid,
    batch_size = 128,
    epochs=20
)

loss, accuracy = model.evaluate(test)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

model.save('tumor.h5')

#test accuracy 0.9399