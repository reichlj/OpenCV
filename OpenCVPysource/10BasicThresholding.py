import cv2

img = cv2.imread('images/black_to_white.jpeg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)
# 0 if img <=128 else 255
_, threshold_binary = cv2.threshold(img, 128,255,cv2.THRESH_BINARY)
# 255 if img <=128 else 0
_, threshold_binary_inv = cv2.threshold(img, 128,255,cv2.THRESH_BINARY_INV)
# img if img <=128 else 128, max irrelevant
_, threshold_binary_trunc = cv2.threshold(img, 128,255,cv2.THRESH_TRUNC)
# 0 if img <=128 else img,
_, threshold_to_zero = cv2.threshold(img, 128,255,cv2.THRESH_TOZERO)
# img if img <=128 else 0
_, threshold_to_zero_inv = cv2.threshold(img, 128,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('threshold_binary',threshold_binary)
cv2.imshow('threshold_binary_inv',threshold_binary_inv)
cv2.imshow('threshold_binary_trunc',threshold_binary_trunc)
cv2.imshow('threshold_to_zero',threshold_to_zero)
cv2.imshow('threshold_to_zero_inv',threshold_to_zero_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()