import cv2 as cv
import time
from timeit import Timer

img1 = cv.imread('images/messi5.png')
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )

img1 = cv.imread('images/messi5.png')
t1 = time.time()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
t2 = time.time()
print( t2-t1 )

img = cv.imread('images/messi5.png')
cv.setUseOptimized(True)
t1 = time.time()
img1 = cv.medianBlur(img1,i)
t2 = time.time()
print('Optimzed=True', t2-t1 )
img = cv.imread('images/messi5.png')

cv.setUseOptimized(False)
t1 = time.time()
img1 = cv.medianBlur(img1,i)
t2 = time.time()
print('Optimzed=False', t2-t1 )

# check if optimization is enabled
img = cv.imread('images/messi5.png')
cv.setUseOptimized(True)
print(cv.useOptimized())
t1 = Timer("cv.medianBlur(img,49)",'import cv2 as cv; from __main__ import img')
print(t1.timeit(20))

# Disable it
img = cv.imread('images/messi5.png')
t2 = Timer("cv.medianBlur(img,49)",'import cv2 as cv; cv.setUseOptimized(False); from __main__ import img')
print(t2.timeit(20))

