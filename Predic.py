import cv2
import tensorflow as tf

CATEGORIES = ["up","down"]


def prepare(filepath):
    IMG_SIZE = 50 # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("1150.mode")


name = 'data/IMG_20190402_150103.jpg'
prediction = model.predict([prepare(name)])
    
print(CATEGORIES[int(prediction[0][0])])