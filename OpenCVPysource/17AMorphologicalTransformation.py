# Morphological Transformation: remove noise from an image
# dilate (erweitern) - expanding shapes contained in input image
# increase/expand shape contained in the image, fill holes
#   dst(x,y) = max src(x+x′,y+y′)
#              (x′,y′):element(x′,y′)≠0
# erode (abtragen) - separate objects
# reduce the shape of an image - erode the boundaries of foreground objects
#   dst(x,y) = min src(x+x′,y+y′)
#              (x′,y′):element(x′,y′)≠0

import cv2
import numpy as np

img = cv2.imread('images/orange.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('images/balls.jpg',cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(mask,kernel)
erosion = cv2.erode(mask,kernel,iterations=1)

cv2.imshow('Image',img)
cv2.imshow('Mask',mask)
cv2.imshow('Dilation',dilation)
cv2.imshow('Erosion',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
