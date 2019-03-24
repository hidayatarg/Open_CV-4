import numpy as np 
import cv2

# 0 array
# image with 150px tall, 200 width, one chanel, type of image
black = np.zeros([100, 200, 1], 'uint8')

# show the image
cv2.imshow("black", black)

# see first pixel values
print(black[0, 0, : ])

ones = np.ones([150,200,3],'uint8')
cv2.imshow("Ones",ones)
print(ones[0, 0, :])

# Print white
white = np.ones([150, 200, 3], 'uint16')
white *= (2**16-1)
cv2.imshow("White", white)
print(white[0, 0, :])


# deep copy of color
color = ones.copy()
# set the pixel
color[:,:] =(255, 0, 0)
cv2.imshow("Blue", color)
print(color[0, 0, :])

# hang user screen
cv2.waitKey(0)
cv2.destroyAllWindows()
