from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image", image)
# to manipulate pixels in image
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) -Red: {}, Green: {},Blue: {}".format(r,g,b))

# to change the color of the pixel located at (0.0) in the image
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red:{}, Green: {}, Blue: {}".format(r, g, b))
# changing pixel values of certain portion of the image
corner = image[300:500, 300:500]
cv2.imshow("Corner", corner)

image[300:500, 300:500] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)
