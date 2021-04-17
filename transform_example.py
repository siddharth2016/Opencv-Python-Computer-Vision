from transform import four_point_transform
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image file")
ap.add_argument("-c", "--coords", help="comma separated list of source points")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
pts = np.array(eval(args["coords"]), dtype="float32")

warp = four_point_transform(image, pts)

cv2.imshow("Original", image)
cv2.imshow("Warped", warp)
cv2.waitKey(0)
cv2.destroyAllWindows()
