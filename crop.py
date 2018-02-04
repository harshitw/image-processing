# cropping the image

import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

cropped = image[60:300, 330:525]
cv2.imshow("bebe Face", cropped)
cv2.waitKey(0)

### zoom out not done !!!
