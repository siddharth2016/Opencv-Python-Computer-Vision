# Image Slide Show using addWeighted

import cv2
import numpy as np
import os

# Getting images from image base
dst = "/home/siddharth/Desktop/PROGRAMS/Work/Opencv exercise/ 0. Image Base/"
images = os.listdir(dst)
length = len(images)

#print(images)

result = cv2.imread(dst + images[0])
i = 1
count = 0

# Slide Show Loop
while(True):
    a = 1.0
    b = 0.0
    img = cv2.imread(dst + images[i])
    
    # Image Transition from one to another
    while(int(b)!=1):
        result = cv2.addWeighted(result, a, img, b, 0)
        cv2.imshow("slideShow", result)
        a -= 0.0001
        b += 0.0001
        
    i = (i+1)%length    # Getting new image from directory

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
