import cv2
import numpy as np
# parallel lines will be parallel - 3 points required
# described by 2*3 matrix

img = cv2.imread('images/grid.jpg')
rows, cols,ch = img.shape
cv2.circle(img,(83,89),5,(0,0,255),-1)  # top -left
cv2.circle(img,(447,89),5,(0,0,255),-1) # top - right
cv2.circle(img,(83,472),5,(0,0,255),-1) # bottom - left
pts1 = np.float32([[83,89],[447,89],[83,472]])
pts2 = np.float32([[83,89],[447,89],[150,472]])
matrix = cv2.getAffineTransform(pts1,pts2)   # 2*3 matrix
result = cv2.warpAffine(img,matrix, (cols,rows))

cv2.imshow('image',img)
cv2.imshow('Affine Transformation',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
