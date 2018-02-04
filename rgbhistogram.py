### Plant classification
# QUANTIFY FLOWER SPECIES USING A 3D RGB HISTOGRAM
# THIS HISTOGRAM IS USED TO CHARECTARIZE THE COLOR OF FLOWER PETALS
# So basically flowers are classfied on the basis of their color

import cv2

class RGBHistogram: ## to encapsualte how flower images are classified
    def __init__(self, bins):
        self.bins = bins # a list containing the number of bins for the 3D histogram

    def describe(self, image, mask = None):
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 256, 0, 256, 0, 256])
        cv2.normalize(hist, hist)
        return hist.flatten()
