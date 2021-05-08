import cv2
import numpy as np

def nothing():
    pass

img = cv2.imread('images/red_panda.jpg', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Image')
cv2.createTrackbar('Threshold value','Image',128,255,nothing)
while True:
    value_threshold = cv2.getTrackbarPos('Threshold value','Image')
    # 0 if img <=value_threshold else 255
    _, threshold_binary = cv2.threshold(img, value_threshold,255,cv2.THRESH_BINARY)
    # 255 if img <=value_threshold else 0
    _, threshold_binary_inv = cv2.threshold(img, value_threshold,255,cv2.THRESH_BINARY_INV)
    # img if img <=value_threshold else value_threshold
    _, threshold_binary_trunc = cv2.threshold(img, value_threshold,255,cv2.THRESH_TRUNC)
    # 0 if img <=value_threshold else img
    _, threshold_to_zero = cv2.threshold(img, value_threshold,255,cv2.THRESH_TOZERO)
    # img if img <=value_threshold else 0
    _, threshold_to_zero_inv = cv2.threshold(img, value_threshold,255,cv2.THRESH_TOZERO_INV)

    cv2.imshow('threshold_binary',threshold_binary)
    cv2.imshow('threshold_binary_inv',threshold_binary_inv)
    cv2.imshow('threshold_binary_trunc',threshold_binary_trunc)
    cv2.imshow('threshold_to_zero',threshold_to_zero)
    cv2.imshow('threshold_to_zero_inv',threshold_to_zero_inv)
    key =cv2.waitKey(100)
    if key == 27:
        break
cv2.destroyAllWindows()