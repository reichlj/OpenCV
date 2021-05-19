import cv2
import numpy as np

def mouse_drawing(event,x,y,flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left Click Down:', x, y)
        circles.append((x, y))
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        # fast Down Up Down Up                 slow Down Up Down Up
        #      cv2.EVENT_LBUTTONDOWN                cv2.EVENT_LBUTTONDOWN
        #           cv2.EVENT_LBUTTONUP                  cv2.EVENT_LBUTTONUP
        #              cv2.EVENT_LBUTTONDBLCLK              cv2.EVENT_LBUTTONDOWN
        #                   cv2.EVENT_LBUTTONUP                  cv2.EVENT_LBUTTONUP
        print('Left Double Click:',x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        print('Left Click Up:', x, y)
        circles.append((x,y))

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',mouse_drawing)

circles = []

while True:
    _, frame = cap.read()
    #for center_positions in circles:
    #    cv2.circle(frame,center_positions,5,(0,0,255),-1)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
    elif key == ord('d'):
        circles = []

cap.release()
cv2.destroyAllWindows()