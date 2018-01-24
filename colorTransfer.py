import numpy as np
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image1", help="path to image")
ap.add_argument("-c", "--image2", help="path to image")
args = vars(ap.parse_args())

def stats(image):

    (l, a, b) = cv2.split(image)
    (lmean, lstd) = (l.mean(), l.std())
    (amean, astd) = (a.mean(), a.std())
    (bmean, bstd) = (b.mean(), b.std())

    return (lmean, lstd, amean, astd, bmean, bstd)
    
def color_transfer(src, dst):

    src = cv2.cvtColor(src, cv2.COLOR_BGR2LAB).astype("float32")
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2LAB).astype("float32")

    (lMeansrc, lStdsrc, aMeansrc, aStdsrc, bMeansrc, bStdsrc) = stats(src)
    (lMeandst, lStddst, aMeandst, aStddst, bMeandst, bStddst) = stats(dst)

    (l, a, b) = cv2.split(dst)
    l -= lMeandst
    a -= aMeandst
    b -= bMeandst

    l = (lStddst/lStdsrc)*l
    a = (aStddst/aStdsrc)*a
    b = (bStddst/bStdsrc)*b

    l += lMeansrc
    a += aMeansrc
    b += bMeansrc

    l = np.clip(l, 0 ,255)
    a = np.clip(a, 0 ,255)
    b = np.clip(b, 0 ,255)

    transfered = cv2.merge([l, a, b])
    transfered = cv2.cvtColor(transfered.astype("uint8"), cv2.COLOR_LAB2BGR)

    return transfered

source = cv2.imread(args["image1"])
dest = cv2.imread(args["image2"])
transferedimg = color_transfer(source, dest)
source = imutils.resize(source, width = 400, height = 400)
dest = imutils.resize(dest, width = 400, height = 400)
transferedimg = imutils.resize(transferedimg, width = 400, height = 400)
cv2.imshow("source", source)
cv2.imshow("destination", dest)
cv2.imshow("transferedimg", transferedimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
