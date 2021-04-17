# Import necessary libraries

import cv2
import numpy as np
import imutils

# Define your Brocade class
class Brocade:

    def __init__(self, imageName):
        self._img = cv2.imread(imageName, cv2.IMREAD_COLOR)
        self._img = imutils.resize(self._img, 600)
        self._grayimg = cv2.cvtColor(self._img, cv2.COLOR_BGR2GRAY)

        # Kernel to Brocade the image
        self._kernel3 = np.array([[-2, -1, 0],
                                  [-1, 1, 1],
                                  [0, 1, 2]], dtype = np.float64)

    def getOrigImg(self):
        return self._img
    def getGrayImg(self):
        return self._grayimg
    
    # Member function to apply kernel on Filter of CV
    def applyFilter(self):
        img = self._img.copy()
        filtered = cv2.filter2D(img, -1, self._kernel3)

        return filtered


# Now real work :> !
if __name__ == "__main__":
    
    B = Brocade("naruto.jpg")
    img = B.getOrigImg()
    grayimg = B.getGrayImg()
    filtered = B.applyFilter()  # filter2D uses Correlation

    res = np.hstack((img, filtered))    # Join Original and filtered image
    
    cv2.imshow("Result", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
