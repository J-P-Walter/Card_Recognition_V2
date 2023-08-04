import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

#MNIST Model from:
#https://www.kaggle.com/code/achintyatripathi/emnist-letter-dataset-97-9-acc-val-acc-91-78
model = tf.keras.models.load_model('models/my_model.keras')
# model.summary()

def getPrediction(img):
    resized = 255-resize_to_28x28(img)
    try:
        res = model.predict(resized)
        return res
    except Exception as error:
        # print("An exception occurred:", error)
        pass
    
#From https://stackoverflow.com/questions/66711654/converting-image-into-mnist-format
#Seems to work, but I think my inputs are the reason the ml model isn't working
def resize_to_28x28(img):
    try:
        img_h, img_w = img.shape
        dim_size_max = max(img.shape)

        if dim_size_max == img_w:
            im_h = (28 * img_h) // img_w
            if im_h <= 0 or img_w <= 0:
                print("Invalid Image Dimention: ", im_h, img_w, img_h)
            tmp_img = cv2.resize(img, (28,im_h),0,0,cv2.INTER_NEAREST)
        else:
            im_w = (28 * img_w) // img_h
            if im_w <= 0 or img_h <= 0:
                print("Invalid Image Dimention: ", im_w, img_w, img_h)
            tmp_img = cv2.resize(img, (im_w, 28),0,0,cv2.INTER_NEAREST)

        out_img = np.zeros((28, 28), dtype=np.ubyte)

        nb_h, nb_w = out_img.shape
        na_h, na_w = tmp_img.shape
        y_min = (nb_w) // 2 - (na_w // 2)
        y_max = y_min + na_w
        x_min = (nb_h) // 2 - (na_h // 2)
        x_max = x_min + na_h

        out_img[x_min:x_max, y_min:y_max] = tmp_img

        return out_img
    except Exception as error:
        # print("An exception occurred:", error)
        pass