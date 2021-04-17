# Program to read and display the image

import numpy as np
import cv2

img = cv2.imread("1.jpg")   # Image name in parentheses
cv2.imshow("1.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Writing it with different name
cv2.imwrite("1_1.jpg", img)

#grayscale image conversion
gray = cv2.imread("1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("gray image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Byte array
#byteary = bytearray(img)
#print(byteary)

#random image
img1 = np.random.randint(0,256,120000).reshape(300,400)
cv2.imshow("im1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
