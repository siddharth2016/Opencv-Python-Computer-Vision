import numpy as np
import cv2
import pyautogui
import imutils

image = pyautogui.screenshot()
image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("image_taken.jpg", image)
image = cv2.imread("image_taken.jpg")
cv2.imshow("Screenshot", imutils.resize(image, width = 600, height=600))
cv2.waitKey(0)
cv2.destroyAllWindows()
