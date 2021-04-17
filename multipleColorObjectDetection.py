import cv2
import numpy as np

cap = cv2.VideoCapture(0)

blower = np.array([80, 100, 100])
bupper = np.array([120, 255, 255])

glower = np.array([30, 100, 100])
gupper = np.array([60, 255, 255])

rlower = np.array([0, 100, 100])
rupper = np.array([10, 255, 255])

while(True):
    _, frame = cap.read()
    imghsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    bmask = cv2.inRange(imghsv, blower, bupper)
    bimg = cv2.bitwise_and(frame, frame, mask = bmask)
    #cv2.imshow("bimg", bimg)

    gmask = cv2.inRange(imghsv, glower, gupper)
    gimg = cv2.bitwise_and(frame, frame, mask = gmask)
    #cv2.imshow("gimg", gimg)

    rmask = cv2.inRange(imghsv, rlower, rupper)
    rimg = cv2.bitwise_and(frame, frame, mask = rmask)
    #cv2.imshow("rimg", rimg)

    res = cv2.add(bimg, gimg)
    res = cv2.add(res, rimg)
    cv2.imshow("Result", res)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
