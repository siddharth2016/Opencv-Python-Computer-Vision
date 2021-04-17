import cv2
import pickle
import numpy as np
from featureVector import featureVector
import os
#Training our dataset
data_dir = 'day1_dataset/'
#getting list of images
images = os.listdir(data_dir)
#print(images)

trained_data = {}
features = featureVector([4,4,4])
for imgs in images:
    if imgs=='Thumbs.db':
        continue
    im_dir = data_dir + imgs
    im = cv2.imread(im_dir, cv2.IMREAD_COLOR)
    print(im_dir)
    feat = features.calHist(im)
    trained_data[im_dir] = feat
print(trained_data)
file = open('trained_data.pickle', 'wb')
pickle.dump(trained_data,file)
file.close()

