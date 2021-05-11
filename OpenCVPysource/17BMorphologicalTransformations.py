import cv2
import numpy as np

def nothing():
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('Trackbars')
# detect yellow marker
cv2.createTrackbar('L - H','Trackbars',24,179,nothing)
cv2.createTrackbar('L - S','Trackbars',0,255,nothing)
cv2.createTrackbar('L - V','Trackbars',0,255,nothing)
cv2.createTrackbar('U - H','Trackbars',40,179,nothing)
cv2.createTrackbar('U - S','Trackbars',255,255,nothing)
cv2.createTrackbar('U - V','Trackbars',255,255,nothing)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos('L - H','Trackbars')
    l_s = cv2.getTrackbarPos('L - S','Trackbars')
    l_v = cv2.getTrackbarPos('L - V','Trackbars')
    u_h = cv2.getTrackbarPos('U - H','Trackbars')
    u_s = cv2.getTrackbarPos('U - S','Trackbars')
    u_v = cv2.getTrackbarPos('U - V','Trackbars')
    lower_blue = np.array([l_h,l_s,l_v])
    upper_blue = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask,kernel)
    dilation = cv2.dilate(mask,kernel)

    #first erosion then dilation - remove noise from image
    opening= cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    #first dilation then erosion
    # closing holes in the foreground object
    closing= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    result = cv2.bitwise_and(frame,frame,mask)

    cv2.imshow('Frame',hsv)
    cv2.imshow('Mask',mask)
    cv2.imshow('Erosion',erosion)
    cv2.imshow('Dilation',dilation)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)
    cv2.imshow('Result',result)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
