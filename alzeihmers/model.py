import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.applications import VGG19
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D, Activation, GlobalAveragePooling2D, BatchNormalization

data_gen=ImageDataGenerator(rescale=1./255, validation_split=0.2)

base_layer=VGG19(include_top=False,  input_shape = (224,224,3))

for layer in base_layer.layers:
    layer.trainable=False


train= data_gen.flow_from_directory(
    directory= "alzeihmers/train",
    target_size=(224,224),
    batch_size=32,
    shuffle=True,
    subset='training',

)

valid=data_gen.flow_from_directory(
    directory= "alzeihmers/train",
    target_size=(224,224),
    batch_size=32,
    subset='validation'
)

test=data_gen.flow_from_directory(
    directory= "alzeihmers/test",
    target_size=(224,224),
    batch_size=2
)


model = Sequential()
model.add(Conv2D(16, (3, 3), activation='relu', input_shape=(224,224,3))),
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(4, activation='softmax'))
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
    
print(model.summary())
early_stopping = keras.callbacks.EarlyStopping(
    patience=10,
    min_delta=0.001,
    restore_best_weights=True)


history = model.fit(
    train,
    validation_data= valid,
    validation_split=0.2,
    batch_size = 32,
    epochs=16
)

loss, accuracy = model.evaluate(test)

print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

model.save('alzeihmers.h5')
#79% acurracy

