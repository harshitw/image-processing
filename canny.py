## canny edge detector
# canny edge detector is a multi step process. It involves blurring
# the image to remove noise, computing Sobel gradient images in x and y
# direction, supperesing edges and finally hysteresis thresholding stage
# that determines if pixel is edge-like or not.

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

# arguments are blurred image, thershold 1, threshold 2
# Any value larger than threshold 2 is considered to be an edge
# Any value lesser than threshold 1 is considered not an edge
# for values lying betweeen thresh 1 and thresh 2 is classified as edge or not edge based on how their intensities are connected
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
