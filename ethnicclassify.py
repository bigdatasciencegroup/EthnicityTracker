import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import *
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator

trainPath='Train'
testPath='Test'
validPath='Valid'

trainBatches = ImageDataGenerator().flow_from_directory(trainPath, target_size=(224,224), classes=['Training Africa', 'Training America', 'Training Arab', 'Training Asian', 'Training Indian'], batch_size=32)
testBatches = ImageDataGenerator().flow_from_directory(testPath, target_size=(224,224), classes=['Testing Africa', 'Testing America', 'Testing Arab', 'Testing Asian', 'Testing Indian'], batch_size=50)
validBatches = ImageDataGenerator().flow_from_directory(validPath, target_size=(224,224), classes=['Valid Africa', 'Valid America', 'Valid Arab', 'Valid Asian', 'Valid Indian'], batch_size=30)
print((trainBatches))
imgs, labels = next(trainBatches)
model = Sequential()

model.add(Conv2D(32,(3,3), activation='relu', input_shape=(224,224,3)))
model.add(Flatten())
model.add(Dense(5, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit_generator(trainBatches, steps_per_epoch=5, validation_data=validBatches, validation_steps=5, epochs=50,verbose=2)