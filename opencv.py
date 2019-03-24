import numpy
import cv2

img = cv2.imread("open-cv.png")

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

# Write the image to a file  
cv2.imwrite("output.jpg", img)

# Ready to show image
# wait for specifed minutes
cv2.waitKey(0)



