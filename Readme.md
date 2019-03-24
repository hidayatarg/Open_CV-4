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