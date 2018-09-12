import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import *
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator

trainPath='Data/Train'
testPath='Data/Test'
validPath='Data/Valid'
practiceTrainPath='Data/PracticeTrain'
practiceTestPath='Data/PracticeTest'
practiceValidPath='Data/PracticeValid'
trainBatches = ImageDataGenerator().flow_from_directory(trainPath, target_size=(224,224), classes=['African', 'American', 'Arab', 'Asian', 'Indian'], batch_size=64)
testBatches = ImageDataGenerator().flow_from_directory(testPath, target_size=(224,224), classes=['African', 'American', 'Arab', 'Asian', 'Indian'], batch_size=32)
validBatches = ImageDataGenerator().flow_from_directory(validPath, target_size=(224,224), classes=['African', 'American', 'Arab', 'Asian', 'Indian'], batch_size=32)

practiceTrainBatches = ImageDataGenerator().flow_from_directory(practiceTrainPath, target_size=(224,224), classes=['Cats','Dogs'], batch_size=64)
practiceTestBatches = ImageDataGenerator().flow_from_directory(practiceTestPath, target_size=(224,224), classes=['Cats','Dogs'], batch_size=32)
practiceValidBatches = ImageDataGenerator().flow_from_directory(practiceValidPath, target_size=(224,224), classes=['Cats','Dogs'], batch_size=32)
print((trainBatches))
imgs, labels = next(trainBatches)
if K.image_data_format() == 'channels_first':
    input_shape = (3, 224, 224)
else:
    input_shape = (224, 224, 3)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Dense(2,ctivation='relu'))
model.add(Activation(2, 'sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
model.fit_generator(practiceTrainBatches, steps_per_epoch=5, validation_data=practiceValidBatches, validation_steps=5, epochs=50,verbose=2)