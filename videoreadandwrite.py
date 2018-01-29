# VIDEO READING AND WRITING

import cv2

cap = cv2.VideoCapture("sample.avi")
fps = int(cap.get(cv2.CAP_PROP_FPS))
size = (int(cap.get(3)),
        int(cap.get(4)))
vidwrite = cv2.VideoWriter("sampleOutput.avi",
                           cv2.VideoWriter_fourcc(*'XVID'),
                           fps, size)
grabbed, frame = cap.read()
while grabbed:
    vidwrite.write(frame)
    grabbed, frame = cap.read()

cap.release()
vidwrite.release()
