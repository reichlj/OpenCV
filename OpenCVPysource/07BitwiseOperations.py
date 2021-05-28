import cv2

road = cv2.imread('images/drawing_1.png')
car = cv2.imread('images/drawing_2.png')
cv2.imshow('road', road)
cv2.imshow('car', car)

bit_and = cv2.bitwise_and(road, car)
bit_or = cv2.bitwise_or(road, car)
bit_xor = cv2.bitwise_xor(road, car)
bit_not = cv2.bitwise_not(road)

cv2.imshow('bit_and',bit_and)
cv2.imshow('bit_or',bit_or)
cv2.imshow('bit_xor',bit_xor)
cv2.imshow('bit_not',bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
