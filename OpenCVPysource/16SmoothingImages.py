import cv2

#img = cv2.imread('images/early_1800.jpg')
#img = cv2.imread('images/balloons_noisy.png')
img = cv2.imread('images/carpet.jpg')
averaging = cv2.blur(img,(5,5))
gaussian = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5,0)
# reduce unwanted noise very well while keeping edges fairly sharp
bilateral = cv2.bilateralFilter(img,5,250,250)

cv2.imshow('Original image',img)
cv2.imshow('Averaging',averaging)
cv2.imshow('Gaussian',gaussian)
cv2.imshow('Median',median)
cv2.imshow('Bilateral',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
