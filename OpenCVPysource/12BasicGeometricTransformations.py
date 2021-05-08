import cv2
import numpy as np

img = cv2.imread('images/red_panda.jpg')
rows, cols, channels = img.shape
print('Height:',rows)
print('Columns:',cols)
scaled_img = cv2.resize(img, (400,500)) # define size explicitly
scaled_img = cv2.resize(img, None, fx=1/3, fy=1/3) # define scale
#                       x-shift  y-shift
#                       right    down
matrix_trans = np.float32([[1,0,25],[0,1,75]])
translated_img = cv2.warpAffine(img,matrix_trans, (cols,rows))  # 2*3 matrix
#                                        center    angle scale
matrix_rot = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
rotated_img = cv2.warpAffine(img,matrix_rot, (cols,rows))


cv2.imshow('Original Image', img)
cv2.imshow('Scaled Image', scaled_img)
cv2.imshow('Translated Image', translated_img)
cv2.imshow('Rotated Image', rotated_img)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
