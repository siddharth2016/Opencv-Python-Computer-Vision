import cv2
import numpy as np

class featureVector:
    def __init__(self, bins):       #bins should be a list ex- [8,8,8]
        self.bins = bins
    def calHist(self, image):
        hist = cv2.calcHist([image], [0,1,2], None, self.bins, [0,256,0,256,0,256])
        hist = cv2.normalize(hist, hist)
        return hist.flatten()
