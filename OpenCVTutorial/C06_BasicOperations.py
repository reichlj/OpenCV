import numpy as np
import cv2 as cv
img = cv.imread('images/messi5.png')
px = img[100,100]
print( px )
# accessing only blue pixel
blue = img[100,100,0]
print( blue )

replicate = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
print(img.shape)
print(replicate.shape)