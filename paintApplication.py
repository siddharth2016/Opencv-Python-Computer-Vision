# PAINT APPLICATION WITH ADJUSTABLE COLOR AND BRUSH SIZE

import cv2
import numpy as np

draw = False
window_name = "Paint Brush Application"
color_win_position = [(400, 30), (490,90)]
bgr_track = {'B': 0, 'G': 0, 'R': 0}

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(window_name)

# Initial color window, showing black
cv2.rectangle(img, color_win_position[0], color_win_position[1], (0,0,0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "R: ", (10, 30), font, 0.5, (255,255,255), 1)
img = cv2.putText(img, "G: ", (90, 30), font, 0.5, (255,255,255), 1)
img = cv2.putText(img, "B: ", (170, 30), font, 0.5, (255,255,255), 1)

img = cv2.putText(img, "0", (30, 30), font, 0.5, (255,255,255), 1)
img = cv2.putText(img, "0", (110, 30), font, 0.5, (255,255,255), 1)
img = cv2.putText(img, "0", (190, 30), font, 0.5, (255,255,255), 1)

def nothing(x):
    pass

def update_R_value(x):
    global font, img, bgr_track
    img = cv2.putText(img, f"{bgr_track['R']}", (30, 30), font, 0.5, (0,0,0), 1)
    img = cv2.putText(img, f"{x}", (30, 30), font, 0.5, (255,255,255), 1)
    bgr_track['R'] = x

def update_G_value(x):
    global font, img, bgr_track
    img = cv2.putText(img, f"{bgr_track['G']}", (110, 30), font, 0.5, (0,0,0), 1)
    img = cv2.putText(img, f"{x}", (110, 30), font, 0.5, (255,255,255), 1)
    bgr_track['G'] = x

def update_B_value(x):
    global font, img, bgr_track
    img = cv2.putText(img, f"{bgr_track['B']}", (190, 30), font, 0.5, (0,0,0), 1)
    img = cv2.putText(img, f"{x}", (190, 30), font, 0.5, (255,255,255), 1)
    bgr_track['B'] = x

def draw_circle(event, x, y, flags, param):
    global draw, img

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.circle(img, (x,y), cv2.getTrackbarPos("Brush Size", window_name),
                       (cv2.getTrackbarPos("B", window_name),
                        cv2.getTrackbarPos("G", window_name),
                        cv2.getTrackbarPos("R", window_name)),
                       -1)

    elif event==cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.circle(img, (x,y), cv2.getTrackbarPos("Brush Size", window_name),
                       (cv2.getTrackbarPos("B", window_name),
                        cv2.getTrackbarPos("G", window_name),
                        cv2.getTrackbarPos("R", window_name)),
                       -1)

cv2.createTrackbar("R", window_name, 0 ,255, update_R_value)
cv2.createTrackbar("G", window_name, 0, 255, update_G_value)
cv2.createTrackbar("B", window_name, 0, 255, update_B_value)
cv2.createTrackbar("Brush Size", window_name, 1, 8, nothing)
cv2.setMouseCallback(window_name, draw_circle)

while(1):
    cv2.imshow(window_name, img)
    key = cv2.waitKey(1) & 0xff
    if key==ord('q'):
        break

    b = cv2.getTrackbarPos("B", window_name)
    g = cv2.getTrackbarPos("G", window_name)
    r = cv2.getTrackbarPos("R", window_name)
    cv2.rectangle(img, color_win_position[0], color_win_position[1], (b,g,r), -1)

cv2.destroyAllWindows()
