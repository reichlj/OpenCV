import cv2

road = cv2.imread('images/road.jpg')
car = cv2.imread('images/car.jpg')

car_gray = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)

print(road[0, 0], car[0, 0])
# dst =	cv.add(	src1, src2[, dst[, mask[, dtype]]] )
sum = cv2.add(road, car) # saturated add
print(sum[0,0])

# dst =	cv.addWeighted(	src1, alpha, src2, beta, gamma[, dst[, dtype]])
#          dst = saturate(src1*alpha + src2*beta + gamma)
#                              alpha   beta gamma
weighted = cv2.addWeighted(road, 1, car, 0.2, 0)

# retval, dst	=	cv.threshold(	src, thresh, maxval, type[, dst]	)
#         THRES_BINARY           maxval if src(x,y)>thresh, 0 otherwise
#         THRES_BINARY_INV       0 if src(x,y)>thresh, maxval otherwise
#                                   thresh  maxval
ret, mask = cv2.threshold(car_gray, 245, 255, cv2.THRESH_BINARY_INV)
sum = cv2.add(car, car, mask=mask)

cv2.imshow('Road', road)
cv2.imshow('car', car)
cv2.imshow('Sum',sum)
cv2.imshow('Weighted',weighted)
cv2.imshow('Gray', car_gray)
cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()