# Open Cv
Open Computer vision library (Open CV) is one the of the widely used image processing library. 
It is open source and cross platform packed with image processing algorithm

```python
# Importing packages
import numpy
import cv2

# Variable to store the import image
img = cv2.imread("open-cv.png")

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

# Ready to show image
# wait for specifed minutes
cv2.waitKey(0)
```

Now we will write this image to a file or even change its extension. Pay attention it should be before `cv2.waitKey(0)` or else the code will not run 

```python
# Write the image to a file  
cv2.imwrite("output.jpg", img)
```
All script: 
```python
# Importing packages
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
```

## Access and Understand Pixels
Print the img variable it will print the pixels of image. And it is type of numpy array. 
```python
import numpy
import cv2
# 1 means using the default colors and channels

img = cv2.imread("open-cv.png", 1)

print(img)

# type of image 
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
```

## Data Types and Structures

```python
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

```

When you run the script you can see the black screen on the interface. click on the program window by pressing any key the window will disappear.

We also see the one pixel value that was printed in console (Terminal).


