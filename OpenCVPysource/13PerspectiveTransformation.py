import cv2
import numpy as np
# perspective Transformation : lines will be lines, 4 points required
# described by 3*3 matrix
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    _, frame = cap.read()
    print(frame.shape)
    cv2.circle(frame,(193,107),5,(0,0,255),-1)   # top-left
    cv2.circle(frame,(470,107),5,(0,0,255),-1)   # top-right
    cv2.circle(frame,(65,475),5,(0,0,255),-1)    # bottom-left
    cv2.circle(frame,(640,450),5,(0,0,255),-1)   # bottom-right
    pts1 = np.float32([[193,107],[470,107],[65,475],[640,450]])
    pts2 = np.float32([[0,0],[400,0],[0,600],[400,600]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)       # 3*3 matrix
    result =  cv2.warpPerspective(frame,matrix,(400,600))
    cv2.imshow('Frame',frame)
    cv2.imshow('Result',result)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()