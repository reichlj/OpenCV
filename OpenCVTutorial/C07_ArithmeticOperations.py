import numpy as np
import cv2 as cv

def continue_with_enter(name):
    print(name)
    cv.waitKey(0)
    cv.destroyAllWindows()

x = np.uint8([250])
y = np.uint8([10])
print( cv.add(x,y))
print( x+y )

img1 = cv.imread('images/ml.png')
logo_img = cv.imread('images/opencv-logo.png')
dst = cv.addWeighted(img1, 0.7, logo_img, 0.3, 0)
cv.imshow('dst',dst)
continue_with_enter('dst')

# Load two images
img1 = cv.imread('images/messi5.png')
logo_img = cv.imread('images/opencv-logo.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = logo_img.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
logo_img_gray = cv.cvtColor(logo_img, cv.COLOR_BGR2GRAY)
cv.imshow('logo_img_gray',logo_img_gray)
continue_with_enter('logo_img_gray')

ret, mask = cv.threshold(logo_img_gray, 10, 255, cv.THRESH_BINARY)
cv.imshow('mask',mask)
continue_with_enter('mask')

mask_inv = cv.bitwise_not(mask)
cv.imshow('mask_inv',mask_inv)
continue_with_enter('mask_inv')

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
cv.imshow('img1_bg',img1_bg)
continue_with_enter('img1_bg')

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(logo_img, logo_img, mask = mask)
cv.imshow('img2_fg',img2_fg)
continue_with_enter('img2_fg')

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
continue_with_enter('res')
