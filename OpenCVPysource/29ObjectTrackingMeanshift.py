import cv2

#video = cv2.VideoCapture('videos/flasche.avi')
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
    #ret, frame = video.read()
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv],[0], roi_hist,[0,180],1)
    # Finds an object on a back projection image. It takes the input back
    # projection of an object and the initial position. The mass center in
    # window of the back projection image is computed and the search window
    # center shifts to the mass center.
    # search window size or orientation do not change during the search
    _, track_window = cv2.meanShift(mask,(x,y,width,height),term_criteria)
    x, y, w, h = track_window
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Mask',mask)
    cv2.imshow('Frame',frame)

    key = cv2.waitKey(25)
    if key == 27:
        break

#video.release()
cv2.destroyAllWindows()
print('Ende')
