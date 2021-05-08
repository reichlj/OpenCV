import cv2
import numpy as np

img = cv2.imread('images/book_page.jpg')
_, threshold = cv2.threshold(img,155,255,cv2.THRESH_BINARY)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# create a binary image with values: 0 and maxValue
# 15,12  -  blocksize=15, constant subtracted C=12
# threshold value T(x,y) is a mean of the blockSize×blockSize neighborhood of (x,y) minus C
#     maxValue   if src(x,y)>T(x,y)
mean_c = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,12)
gauss = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,12)
cv2.imshow('Img',img)
cv2.imshow('Img Threshold',threshold)
cv2.imshow('Adaptive Thesholding',mean_c)
cv2.imshow('Adaptive Thesholding Gauss',gauss)
key = cv2.waitKey(0)
cv2.destroyAllWindows()

