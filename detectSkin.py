import imutils
import numpy as np
import cv2

lower = np.array([0,20,30], dtype="uint8")
upper = np.array([90, 255, 255], dtype="uint8")

cap = cv2.VideoCapture(0)

while True:

    grabbed, frame = cap.read()
    if not grabbed:
        break

    frame = imutils.resize(frame, width = 500)
    convert = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(convert, lower, upper)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    skinMask = cv2.erode(skinMask, kernel, iterations = 2)
    skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

    skinMask = cv2.GaussianBlur(skinMask, (3,3), 0)
    skin = cv2.bitwise_and(frame, frame, mask=skinMask)

    cv2.imshow("images", skin)

    if cv2.waitKey(1) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
