import cv2
import numpy as np
img1 = cv2.imread('images/drawing_1.png')
img2 = cv2.imread('images/drawing_2.png')
cv2.imshow('road',img1)
cv2.imshow('car',img2)

bit_and = cv2.bitwise_and(img1,img2)
bit_or = cv2.bitwise_or(img1,img2)
bit_xor = cv2.bitwise_xor(img1,img2)
bit_not = cv2.bitwise_not(img1)

cv2.imshow('bit_and',bit_and)
cv2.imshow('bit_or',bit_or)
cv2.imshow('bit_xor',bit_xor)
cv2.imshow('bit_not',bit_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
