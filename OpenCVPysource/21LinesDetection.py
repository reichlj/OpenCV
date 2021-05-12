import cv2
import numpy as np

img = cv2.imread('images/lines.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,75,150)

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=180)
for count, line in enumerate(lines):
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255-count*12,count*12),3)

print(lines)
print(lines.shape)

cv2.imshow('edges',edges)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
