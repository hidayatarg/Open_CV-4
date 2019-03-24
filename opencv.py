import numpy
import cv2

img = cv2.imread("open-cv.png")

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

# Ready to show image
# wait for specifed minutes
cv2.waitKey(0)
