# VIDEO READING AND WRITING, USE OF WEB-CAM

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
saveCap = cv2.VideoWriter("outputWebCam.avi", fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame, 1)  #will result in same action 
                                    #left/right position same as our position
                                    #not altered - Vertical Flip
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    saveCap.write(frame)
    cv2.imshow("result", gray)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cap.release()
saveCap.release()
cv2.destroyAllWindows()
