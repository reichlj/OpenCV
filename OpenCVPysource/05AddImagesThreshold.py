import cv2

img1 = cv2.imread('images/road.jpg')
img2 = cv2.imread('images/car.jpg')

img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

print(img1[0,0],img2[0,0])
sum = cv2.add(img1,img2) # saturated add
print(sum[0,0])

#          dst = saturate(src1*alpha + src2*beta + gamma)
#                              alpha   beta gamma
weighted = cv2.addWeighted(img1,1,img2,0.2,0)

#         THRES_BINARY           maxval if src(x,y)>thresh, 0 otherwise
#         THRES_BINARY_INV       0 if src(x,y)>thresh, maxval otherwise
#                                   thresh  maxval
ret, mask = cv2.threshold(img2_gray,245, 255,    cv2.THRESH_BINARY_INV)
sum = cv2.add(img2,img2, mask=mask)

cv2.imshow('Road',img1)
cv2.imshow('car',img2)
cv2.imshow('Sum',sum)
cv2.imshow('Weighted',weighted)
cv2.imshow('Gray',img2_gray)
cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()