# PROGRAM TO DRAW CIRCLE AND RECTANGLE WITHOUT FILL

import cv2
import numpy as np
from math import sqrt
draw = False
mode = True
ix=iy=0
fx=fy=0
def draw_figure(event, x, y, flags, param):
    global draw,ix,iy,mode,fx,fy

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            fx,fy = x,y
#            if mode == True:
#                cv2.rectangle(img, (ix,iy), (fx,fy), (0,255,0), 2)
##            else:
##                cv2.circle(img, (x,y), 5, (0,0,255), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False

        if mode == True:
            cv2.rectangle(img, (ix,iy), (fx,fy), (0,255,0), 2)
        else:
            cv2.circle(img, , int(sqrt((ix-fx)**2 + (iy-fy)**2)), (0,0,255), 2)


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_figure)

while(True):

    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xff
    if key==ord('m'):
        mode = not mode

    elif key==ord('q'):
        break

cv2.destroyAllWindows()
