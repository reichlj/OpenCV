import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cv2.namedWindow('Frame')
cv2.createTrackbar('Scale','Frame',11,20,nothing)
cv2.createTrackbar('Neighbours','Frame',0,20,nothing)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    scale = cv2.getTrackbarPos('Scale','Frame')
    neighbours = cv2.getTrackbarPos('Neighbours','Frame')

    faces = face_cascade.detectMultiScale(gray,scale/10,neighbours)
    for rect in faces:
        (x,y,w,h) = rect
        rect = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)


    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

