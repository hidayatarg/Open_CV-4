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