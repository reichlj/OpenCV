import cv2
import numpy as np

blue_pen_template = cv2.imread('images/blue_pen.png', cv2.IMREAD_GRAYSCALE)
h,w = blue_pen_template.shape

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_scale, blue_pen_template, cv2.TM_CCOEFF_NORMED)
    print('max',np.max(result))
    loc = np.where(result>0.7)
    for y,x in zip(*loc):
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
