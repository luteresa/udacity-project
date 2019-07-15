
# coding: utf-8

# In[18]:


import csv
import cv2
import numpy as np


# In[19]:


lines = []
with open('./driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)

images = []
measurements = []
lines = lines[1:-1]
for line in lines:
    source_path = line[0]
    #print(source_path)
    filename = source_path.split('/')[-1]
    #print(filename)
    current_path = '../data/IMG/'+filename
    image = cv2.imread(current_path)
    images.append(image)
    measurement = float(line[3])
    measurements.append(measurement)


# In[20]:


X_train = np.array(images)
y_train = np.array(measurements)


# In[21]:


from keras.models import Sequential
from keras.layers import Flatten, Dense


# In[22]:


model = Sequential()
model.add(Flatten(input_shape=(160,320,30)))
model.add(Dense(1))



# In[23]:



model.compile(loss='mse',optimizer='adam')
model.fit(X_train,y_train,validation_split=0.2,shuffle=True,nb_epoch=7)


# In[ ]:


model.save('model.h5')

