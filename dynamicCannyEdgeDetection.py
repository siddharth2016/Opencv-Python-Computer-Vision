# Dynamic Variation in Canny Edge Detection - by Changing threshold values

import cv2
import numpy as np

def nothing():
    pass

img = cv2.imread("cube.jpg", 0)     #Take the input image in GrayScale

cv2.namedWindow("Cube Canny Edge Detection") #Get a named window

#Set minimum and maximum value trackbar
cv2.createTrackbar("Min Value", "Cube Canny Edge Detection", 0, 100, nothing) 
cv2.createTrackbar("Max Value", "Cube Canny Edge Detection", 0, 200, nothing)

while(True):

    #Get trackbar value from the respective trackbar
    minV = cv2.getTrackbarPos("Min Value", "Cube Canny Edge Detection")
    maxV = cv2.getTrackbarPos("Max Value", "Cube Canny Edge Detection")

    #Apply Canny Edge Detection on obtained minV and maxV
    res = cv2.Canny(img, minV, maxV)
    cv2.imshow("Cube Canny Edge Detection", res)

    #Break when "q" key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
