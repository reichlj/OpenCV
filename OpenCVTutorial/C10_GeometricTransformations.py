import numpy as np
import cv2 as cv

def next_image():
   print('Press q within image to close display')
   z = 0
   while z != ord('q'):  # wait until 'q' is pressed
      z = cv.waitKey(0)  # 0 means wait forever, 5 means wait 5 ms
   cv.destroyAllWindows()

img = cv.imread('images\messi5.png')
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
cv.imshow('Doppelte Größe',res)
next_image()