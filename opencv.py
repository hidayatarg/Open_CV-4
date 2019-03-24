import numpy
import cv2
# 1 means using the default colors and channels
# 0 image will be read black and white
img = cv2.imread("open-cv.png", 1)

print(img)
print(type(img))

# image pixel
print(len(img))

# image top row pixel
print(len(img[0]))

# number of channels in image output: 3 means RGB 
print(len(img[0][0]))

# information about image
# horizontal rows, columns and channels
print(img.shape)

#Type of image (unsigned integer value of eight)
print(img.dtype)

# pixel values at specific array
print(img[10, 5])

# all pixel at one chanel of image
print(img[:, :, 0])

# total number of pixel in this image
print(img.size)



