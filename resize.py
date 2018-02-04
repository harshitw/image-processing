# image resizing

import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# maintaining the proper aspect ratio by dicing new width and old width
r = 150.0 / image.shape[1]
# calculating the new height and converting it into an integer
dim = (150, int(image.shape[0] * r))
# interpolation algorithm works behind the scenes to handle how the actual image is resized
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# can also use INTER_LINEAR, INTER_CUBIC, INTER_NEAREST instead of INTER_AREA
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

resized = imutils.resize(image, width = 100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)
