import cv2
import numpy as np

img = cv2.imread('images/hand.jpg')
#cv2.imshow('Original Image',img)

#first_layer = cv2.pyrDown(img)
#second_layer = cv2.pyrDown(first_layer)
#cv2.imshow('SecondLayer',second_layer)
#cv2.imshow('FirstLayer',first_layer)

# Gaussian Pyramid - reduce size
layer = img.copy()
gaussian_pyramid = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)
#cv2.imshow('Gaussian'+str(0),gaussian_pyramid[0])
#cv2.imshow('Gaussian'+str(5),gaussian_pyramid[5])

# Laplacian Pyramid - expand -size
k=1
if k==0:
    first_layer  = cv2.pyrDown(img)
    expanded_image = cv2.pyrUp(first_layer)
    # subtract the expanded image from the original image
    # image shows edges
    laplacian = cv2.subtract(img,expanded_image)
    cv2.imshow('Original',img)
    cv2.imshow('Laplacian',laplacian)
else:
    layer = gaussian_pyramid[5]
    cv2.imshow('6', layer)
    laplacian_pyramid = [layer]
    for i in range(5,0,-1):
        size = (gaussian_pyramid[i-1].shape[1],gaussian_pyramid[i-1].shape[0])
        gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
        laplacian = cv2.subtract(gaussian_pyramid[i-1],gaussian_expanded)
        laplacian_pyramid.append(laplacian)
        cv2.imshow(str(i),laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()