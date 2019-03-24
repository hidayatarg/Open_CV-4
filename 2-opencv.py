import numpy as np 
import cv2

# 0 array
# image with 150px tall, 200 width, one chanel, type of image
black = np.zeros([100, 200, 1], 'uint8')

# show the image
cv2.imshow("black", black)

# see first pixel values
print(black[0, 0, : ])

# hang user screen
cv2.waitKey(0)
cv2.destroyAllWindows()
