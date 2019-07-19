import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import pickle
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

def make_data():
    DATADIR = "New"

    CATEGORIES = ["up", "down"]

    for category in CATEGORIES:  # do dogs and cats
        path = os.path.join(DATADIR,category)  # create path to dogs and cats
        for img in os.listdir(path):  # iterate over each image per dogs and cats
            img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
            plt.imshow(img_array, cmap='gray')  # graph it
            plt.show()  # display!

            break  # we just want one for now so break
        break  #...and one more!

    IMG_SIZE = 50
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))    

    training_data = []

    def create_training_data():
        for category in CATEGORIES:  # do dogs and cats

            path = os.path.join(DATADIR,category)  # create path to dogs and cats
            class_num = CATEGORIES.index(category)  # get the classification  (0 or a 1). 0=dog 1=cat

            for img in tqdm(os.listdir(path)):  # iterate over each image per dogs and cats
                try:
                    img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
                    training_data.append([new_array, class_num])  # add this to our training_data
                except Exception as e:  
                    pass
   

    create_training_data()

    print(len(training_data))

    X = []
    y = []

    for features,label in training_data:
        X.append(features)
        y.append(label)

    print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)


    pickle_out = open("X.pickle","wb")
    pickle.dump(X, pickle_out)
    pickle_out.close()

    pickle_out = open("y.pickle","wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()

def make_model():
    pickle_in = open("X.pickle","rb")
    X = pickle.load(pickle_in)
    pickle_in = open("y.pickle","rb")
    y = pickle.load(pickle_in)
    X = X/255.0

    model = Sequential()
    model.add(   Conv2D(64, (3, 3), input_shape=X.shape[1:])   )
    model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(256, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    model.compile(loss='binary_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
    model.fit(X, y, batch_size=64, epochs=15, validation_split=0.2)   
    model.save('Detec_mk2_v2.model')

make_model()   