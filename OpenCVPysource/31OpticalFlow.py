import cv2
import numpy as np

# globals
point = None
point_selected = False
old_points = None

def select_point_listener(event, x, y, flags, params):
    global point, point_selected,old_points
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x,y)
        point_selected = True
        old_points = np.array([[x,y]], dtype=np.float32)

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', select_point_listener)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# create old frame
_, frame = cap.read()
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Lucas Kanade Params
lk_params = dict(winSize = (15,15), #size of the search window at each pyramid level
                 maxLevel = 4, #0-based maximal pyramid level number; if set to 0, pyramids are not used (single level), if set to 1, two levels are used
                 criteria = (cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT, 10, 0.03))

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if point_selected is True:
        cv2.circle(frame,point,5,(0,0,255),2)
        # Calculates optical flow for sparse feature set using iterative Lucas-Kanade method with pyramids.
        new_points, status, error = cv2.calcOpticalFlowPyrLK(
            old_gray,   # previous image -f irst 8-bit input image or pyramid constructed by buildOpticalFlowPyramid
            gray_frame, # next image - second input image or pyramid of the same size and the same type as prevImg
            old_points, # vector of 2D points for which the flow needs to be found
            None,
            **lk_params)
        
        old_points = new_points
        x,y = new_points.ravel()
        cv2.circle(frame,(x,y),5,(0,255,0),-1)

    old_gray = gray_frame.copy()
    first_level = cv2.pyrDown(frame)
    cv2.imshow('Frame',frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()