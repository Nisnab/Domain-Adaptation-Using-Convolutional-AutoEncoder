from flask import Flask, render_template
from flask import request

app = Flask(__name__)

import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow as tf
from keras.preprocessing.image import img_to_array
from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.models import Sequential
import os
# import joblib
import pickle

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

UPLOAD_FOLDER = "/home/nisnab/workspace/flaskproject/Flask/static/images/"

url=""
@app.route('/', methods=["GET", "POST"])
def autoencoder():
    SIZE = 256
    url=""
    from tqdm import tqdm
    # Original einstein image for prediction as monalisa
    img_data3 = []
    #
    # img3 = cv2.imread(r'166023.jpg', 1)
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(UPLOAD_FOLDER, image_file.filename)
            print(image_location)
            image_file.save(image_location)
            img3 = cv2.imread(image_location,1)
            img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)  # Changing BGR to RGB to show images in true colors
            img3 = cv2.resize(img3, (SIZE, SIZE))
            img_data3.append(img_to_array(img3))

            img_array3 = np.reshape(img_data3, (len(img_data3), SIZE, SIZE, 3))
            img_array3 = img_array3.astype('float32') / 255.

    # In[3]:

            from tensorflow import keras
            model2 = keras.models.load_model('autoencoder_best_model.h5')

    # In[4]:

            print("Output")
            pred = model2.predict(img_array3)
            plt.imshow(pred[0].reshape(SIZE, SIZE, 3))
            plt.savefig('static/images/'+image_file.filename)
            url='static/images/'+image_file.filename


    return render_template('plot.html', url=url)


if __name__ == '__main__':
    app.run()
