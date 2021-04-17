# CREATING OPENCV SYMBOL USING DRAWING FUNCTIONS

import cv2
import numpy as np

#output image
img = np.full((360, 512, 3), 255, dtype="uint8")

img = cv2.ellipse(img, (256, 80), (60,60), 120,0,300,(0,0,255),-1)
img = cv2.ellipse(img, (256, 80), (20,20), 120,0,300,(255,255,255),-1)
img = cv2.ellipse(img, (176, 200), (60,60), 0,0,300,(0,255,0),-1)
img = cv2.ellipse(img, (176, 200), (20,20), 0,0,300,(255,255,255),-1)
img = cv2.ellipse(img, (336, 200), (60,60), 300,0,300,(255,0,0),-1)
img = cv2.ellipse(img, (336, 200), (20,20), 300,0,300,(255,255,255),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "OpenCV", (196,296), font, 1, (0,0,0), 4, cv2.LINE_AA)

cv2.imshow("OpenCV Logo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('opencvlogo.png', img)