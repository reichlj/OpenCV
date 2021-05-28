import cv2

from matplotlib import pyplot as plt

original_image = cv2.imread('images/goalkeeper.jpg')
hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

roi = cv2.imread('images/pitch_ground.jpg')
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

hue,saturation, value = cv2.split(hsv_roi)
# hue is an 'image' showing the color value
# saturation is an 'image' showing the saturation value

# multidimensional (2d) Histogram ROI
#                      list of source arrays
#                                   channels
#                                         mask
#                                               histogram sizes in each dimension
#                                                         ranges in each dimension
#                                                          l0,u0, l1,u1
roi_hist = cv2.calcHist([hsv_roi], [0,1], None, [180,256], [0,180,0,256])
mask = cv2.calcBackProject([hsv_original],[0,1],roi_hist,[0,180,0,256],1)

# Filtering remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
mask = cv2.filter2D(mask,-1,kernel=kernel)
_, mask = cv2.threshold(mask,50,255,cv2.THRESH_BINARY)
mask = cv2.merge((mask,mask,mask))
result = cv2.bitwise_and(original_image, mask)

cv2.imshow('Result', result)
cv2.imshow('Mask',mask)
cv2.imshow('Original Image', original_image)
cv2.imshow('ROI',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# show histogram
#plt.imshow(roi_hist)
#plt.show()
