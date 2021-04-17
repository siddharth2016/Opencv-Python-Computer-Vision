# CREATING OPENCV SYMBOL USING DRAWING FUNCTIONS

import cv2
import numpy as np

#output image
img = np.zeros((512,512,3), dtype="uint8")

##cv2.imshow("img",img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

##img = cv2.circle(img, (256,80), 60, (0,0,255), -1)
##img = cv2.circle(img, (256, 80), 20, (0,0,0), -1)
##img = cv2.circle(img, (176, 200), 60, (0,255,0), -1)
##img = cv2.circle(img, (176, 200), 20, (0,0,0), -1)
##img = cv2.circle(img, (336, 200), 60, (255,0,0), -1)
##img = cv2.circle(img, (336, 200), 20, (0,0,0), -1)
##font = cv2.FONT_HERSHEY_SIMPLEX
##img = cv2.putText(img, "OpenCV", (196,296), font, 1, (255,255,255))
##cv2.imshow("img",img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

img = cv2.ellipse(img, (256, 80), (60,60), 120,0,300,(0,0,255),-1)
img = cv2.ellipse(img, (256, 80), (20,20), 120,0,300,(0,0,0),-1)
img = cv2.ellipse(img, (176, 200), (60,60), 0,0,300,(0,255,0),-1)
img = cv2.ellipse(img, (176, 200), (20,20), 0,0,300,(0,0,0),-1)
img = cv2.ellipse(img, (336, 200), (60,60), 300,0,300,(255,0,0),-1)
img = cv2.ellipse(img, (336, 200), (20,20), 300,0,300,(0,0,0),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "OpenCV", (196,296), font, 1, (255,255,255), 4, cv2.LINE_AA)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
