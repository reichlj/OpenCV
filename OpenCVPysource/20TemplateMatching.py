import cv2
import numpy as np

img = cv2.imread("images/simpsons.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('images/barts_face.jpg',cv2.IMREAD_GRAYSCALE)
h, w = template.shape
result = cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.9)  #(r,c)

#for pt in zip(*loc[::-1]):
#   cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0),3)
for (r,c) in zip(*loc):
   cv2.rectangle(img,(c,r),(c+w,r+h),(0,255,0),3)

cv2.imshow("img", img)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()