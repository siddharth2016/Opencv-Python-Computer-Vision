import cv2
import numpy as np
import pandas as pd
from search import searchOn
from featureVector import featureVector

data_dir = 'day1_dataset/index.jpg'
feat = featureVector([4,4,4])
queryimg = cv2.imread(data_dir, cv2.IMREAD_COLOR)
queryimgfeat = feat.calHist(queryimg)
print(len(queryimgfeat))
indx = pd.read_pickle('trained_data.pickle')
#print(indx)
searchImages = searchOn(indx)
result = searchImages.compareWith(queryimgfeat)
print(result)

i=0
for (v, k) in result:
    i+=1
    if i>10:
        break
    im = cv2.imread(k, cv2.IMREAD_COLOR)
    cv2.imshow('image '+str(i), im)
