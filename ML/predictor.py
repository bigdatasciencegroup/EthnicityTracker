import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing import image
from keras import backend as K
from keras import metrics
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

model = load_model('trained_model.h5')
def predictImage(image_name):
    img = image.load_img(image_name, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    prediction = model.predict_classes(x)
    if prediction == 0:
        prediction='Cat'
    else:
        prediction = 'Dog'
    print(prediction)
predictImage('Data/Dog1.jpg')
predictImage('Data/cat1.jpg')
predictImage('Data/Dog2.jpg')
predictImage('Data/Cat2.jpg')
