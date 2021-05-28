import cv2

def nothing(value):
    pass

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cv2.namedWindow('frame')
#    trackbarname	Name of the created trackbar.
#           winname	Name of the window that will be used as a parent of the created trackbar.
#               value	Optional pointer to an integer variable whose value reflects the position of the slider.
#                       Upon creation, the slider position is defined by this variable.
#                   count	Maximal position of the slider. The minimal position is always 0.
#                           onChange	Pointer to the function to be called every time the slider changes position.
#                                       This function should be prototyped as void Foo(int,void*); , where the first
#                                       parameter is the trackbar position and the second parameter is the user data
#                                       (see the next parameter). If the callback is the NULL pointer, no callbacks
#                                       are called, but only value is updated.
cv2.createTrackbar('test','frame',50,500,nothing)
cv2.createTrackbar('color/gray','frame',0,1,nothing)

while True:
    _, frame = cap.read()
    test = cv2.getTrackbarPos('test','frame')
    font = cv2.FONT_ITALIC
    #img = cv.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    cv2.putText(frame,str(test),(50,150),font,3,(0,0,255),5)

    s = cv2.getTrackbarPos('color/gray','frame')
    if s == 0:
        pass
    else:
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()