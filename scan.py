from transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

#Constructing argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to image")
args = vars(ap.parse_args())

#Edge Detection
image = cv2.imread(args["image"])
ratio = image.shape[0]/500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
edged = cv2.Canny(gray, 75, 200)

cv2.imshow("image", image)
cv2.imshow("edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Finding Contours
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse = True)[:5]

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02*peri, True)

    if len(approx)==4:
        screenCnt = approx
        break

cv2.drawContours(image, [screenCnt], -1, (0,255,0), 2)
cv2.imshow("outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
##print(screenCnt)
##print(screenCnt.reshape(4,2)*ratio)

#Four point transfrom and Thresholding
warpImg = four_point_transform(orig, screenCnt.reshape(4,2)*ratio)

warpImg = cv2.cvtColor(warpImg, cv2.COLOR_BGR2GRAY)
T = threshold_local(warpImg, 11, offset = 10, method = "gaussian")
warpImg = (warpImg>T).astype("uint8")*255

cv2.imshow("Original", imutils.resize(orig, height=600))
cv2.imshow("Scanned", imutils.resize(warpImg, height = 600))
cv2.waitKey(0)
