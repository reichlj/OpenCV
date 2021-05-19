import cv2
import numpy as np

first_frame = cv2.imread('videos/flasche_first.jpg')
x=282
y=209
width = 106
height = 114
roi = first_frame[y:y+height,x:x+width]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,179])
roi_hist = cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10 ,1)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv],[0],roi_hist, [0,180],1)
    # finds an object center using meanShift and then adjusts the window size and
    # finds the optimal rotation. The function returns the rotated rectangle
    # structure that includes the object position, size, and orientation
    # ret x,y,w,h, angle
    ret,track_window = cv2.CamShift(mask,(x,y,width,height),term_criteria)
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.polylines(frame,[pts],True,(255,0,0),2)

    cv2.imshow('mask',mask)
    cv2.imshow('Frame',frame)

    key = cv2.waitKey(25)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
print('Ende')

