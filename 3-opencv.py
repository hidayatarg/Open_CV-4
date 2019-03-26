import numpy as np
import cv2

# loading with full color
color = cv2.imread("Blue_morpho_butterfly.jpg", 1)

# show the image
cv2.imshow("Image", color)

# place window at top left corner
cv2.moveWindow("Image", 0, 0)
print(color)

# data about image
height, width, channels = color.shape

# destory with any key
cv2.waitKey(0)
cv2.destroyAllWindows()
