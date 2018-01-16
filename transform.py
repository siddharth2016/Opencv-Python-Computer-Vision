import numpy as np
import cv2

def order_points(pts):
    #ordering the 4-points from top-left to bottom-left
    rect = np.zeros((4,2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    #finding new dimesion for fitting the window
    newWidthTop = np.sqrt((tl[0]-tr[0])**2+(tl[1]-tr[1])**2)
    newWidthBottom = np.sqrt((bl[0]-br[0])**2+(bl[1]-br[1])**2)
    newWidth = max(newWidthTop, newWidthBottom)

    newHeightLeft = np.sqrt((tl[0]-bl[0])**2+(tl[1]-bl[1])**2)
    newHeightRight = np.sqrt((tr[0]-br[0])**2+(tr[1]-br[1])**2)
    newHeight = max(newHeightLeft, newHeightRight)

    dst = np.array([[0,0], [newWidth-1, 0], [newWidth-1,  newHeight-1],
                    [0, newHeight-1]], dtype="float32")

    Matrix = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(image, Matrix, (int(newWidth), int(newHeight)))

    return warp

