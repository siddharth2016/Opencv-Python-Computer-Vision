# PAINT APPLICATION WITH ADJUSTABLE COLOR AND BRUSH SIZE

import cv2
import numpy as np
draw = False
#ix=iy=0

def nothing(x):
    pass

def draw_circle(event, x, y, flags, param):
    global draw

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.circle(img, (x,y), cv2.getTrackbarPos("Brush Size", "image"),
                       (cv2.getTrackbarPos("B", "image"),
                        cv2.getTrackbarPos("G", "image"),
                        cv2.getTrackbarPos("R", "image")),
                       -1)
    elif event==cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.circle(img, (x,y), cv2.getTrackbarPos("Brush Size", "image"),
                       (cv2.getTrackbarPos("B", "image"),
                        cv2.getTrackbarPos("G", "image"),
                        cv2.getTrackbarPos("R", "image")),
                       -1)


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("image")

cv2.createTrackbar("R", "image", 0 ,255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)
cv2.createTrackbar("Brush Size", "image", 1, 8, nothing)
cv2.setMouseCallback("image", draw_circle)

while(1):
    cv2.imshow("image", img)
    key = cv2.waitKey(1) & 0xff
    if key==ord('q'):
        break

##    r = cv2.getTrackbarPos("R", "image")
##    g = cv2.getTrackbarPos("G", "image")
##    b = cv2.getTrackbarPos("B", "image")
##    brushSize = cv2.getTrackbarPos("Brush Size", "image")

    
cv2.destroyAllWindows()
