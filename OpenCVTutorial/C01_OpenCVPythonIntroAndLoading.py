import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys

def next_image():
   print('Press q within image to close display')
   z = 0
   while z != ord('q'):  # wait until 'q' is pressed
      z = cv.waitKey(0)  # 0 means wait forever, 5 means wait 5 ms
   cv.destroyAllWindows()

# read a color image
# IMREAD_GRAYSCALE =  0
# IMREAD_COLOR     =  1  cv2 uses 8-Bit BGR - Default
# IMREAD_UNCHANGED = -1
img_bgr = cv.imread('images/watch.jpg', cv.IMREAD_UNCHANGED)
if img_bgr is None:
   sys.exit('Could not read the image.')
cv.imshow('Display color image', img_bgr)
height,width,channel = img_bgr.shape
print(img_bgr.shape,height,width,channel)  # (height:168, width:300,channel:3)
(b,g,r) = img_bgr[1,2]  # CV stores colors using BGR not RGB
next_image()

# grayscale image
img = cv.imread('images/watch.jpg', cv.IMREAD_GRAYSCALE)
# img is a numpy array of type uint8 {ndarray: (168,300)}
cv.imshow('Display Grayscale image', img)
(height,width) = img.shape
print(img.shape,height,width)  # (height:168, width:300)
next_image()

#     y      x
img[50:60,150:190] = 255
cv.imshow('Image with a white bar', img)
next_image()
cv.imwrite('images/watch_bar.jpg', img)

# Matplotlib RGB for color
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.plot([50,100],[80,100],'c', linewidth=5)
#plt.show()