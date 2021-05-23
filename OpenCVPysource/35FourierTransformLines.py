import cv2
import numpy as np

#img =  cv2.imread('images/horizontal_lines.jpg',cv2.IMREAD_GRAYSCALE)
img =  cv2.imread('images/letters/a_0.png',cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
#fshift = f
magnitude_spectrum = 20*np.log(np.abs(fshift))
magnitude_spectrum = np.asarray(magnitude_spectrum,dtype=np.uint8)

print(magnitude_spectrum)

cv2.imshow('magnitude spectrum',magnitude_spectrum)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()