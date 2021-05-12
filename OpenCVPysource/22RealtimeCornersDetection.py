import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('Frame')
cv2.createTrackbar('quality','Frame',1,100,nothing)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    quality = cv2.getTrackbarPos('quality','FRame')
    if quality > 0:
        quality = quality/100
    else:
        quality = 0.01
    corners = cv2.goodFeaturesToTrack(gray,1000,quality,20)
    if corners is not None:
        corners = np.int0(corners)
        print(corners.shape[0])
        for corner in corners:
            x,y = corner.ravel()
            cv2.circle(frame,(x,y),3,(0,0,255),-1)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
print('Frame')

