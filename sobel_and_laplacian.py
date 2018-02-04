### GRADIENTS AND EDGE detection
# using canny edge detector, a multi stage process of noise reduction(blurring), finding the gradient of the image(using sobel kernel in both horizontal and verticacl direction)
## non maximum compression and hysteresis thresholding

# Laplacian and sobel

import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# To compute gradient magnitude image by calling the Laplacian function
lap = cv2.Laplacian(image, cv2.CV_64F)
# Used 64 bit unsigned integer instead of 8 bit integers
# Transition of black to white and white to black image
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)
