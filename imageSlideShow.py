# Image Slide Show using addWeighted

import cv2
import numpy as np
from math import ceil
import os

# Getting images from image base
dst = "./images/"
images = os.listdir(dst)
length = len(images)

result = np.zeros((360,360,3), np.uint8)
i = 1

a = 1.0     # alpha
b = 0.0     # beta
img = cv2.imread(dst + images[i])
img = cv2.resize(img, (360, 360))

# Slide Show Loop
while(True):

    if(ceil(a)==0):
        a = 1.0
        b = 0.0
        i = (i+1)%length    # Getting new image from directory
        img = cv2.imread(dst + images[i])
        img = cv2.resize(img, (360, 360))

    a -= 0.01
    b += 0.01

    # Image Transition from one to another
    result = cv2.addWeighted(result, a, img, b, 0)
    cv2.imshow("Slide Show", result)
    key = cv2.waitKey(1) & 0xff
    if key==ord('q'):
        break

cv2.destroyAllWindows()