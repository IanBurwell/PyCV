import cv2
import numpy as np

#descriptors are nice in classes, because we can set 1 property
#like num_bins for all the images that will use said descriptor

#defines imgs with 3D RGB Histogram
class RGBHist:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, img, mask=None):
        #Calc 3D hist and normalize so
        #a scaled image has roughly same histogram as original
        hist = cv2.calcHist(img, [0, 1, 2], mask, self.bins, [0,256, 0,256, 0,256])
        hist = cv2.normalize(hist, hist)
        #Makes 1D array out of 3D array so it can be a descriptor
        return hist.flatten()
