#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
#use tf_gpu_copy conda env

import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow as tf
from keras.preprocessing.image import img_to_array
from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.models import Sequential
import os
import pickle
SIZE=256
from tqdm import tqdm
#Original einstein image for prediction as monalisa
img_data3=[]

img3=cv2.imread(r'/home/nisnab/workspace/ImageTranslation/Pix2Pix/dataset/facades/train/a/image1002.png', 1)
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)#Changing BGR to RGB to show images in true colors
img3=cv2.resize(img3,(SIZE, SIZE))
img_data3.append(img_to_array(img3))

img_array3 = np.reshape(img_data3, (len(img_data3), SIZE, SIZE, 3))
img_array3 = img_array3.astype('float32') / 255.


# In[3]:


from tensorflow import keras
model2 = keras.models.load_model('autoencoder_best_model.h5')

# In[4]:

print("Output")
pred = model2.predict(img_array3)
plt.imshow(pred[0].reshape(SIZE,SIZE,3))

#plt.show()
# In[ ]:




