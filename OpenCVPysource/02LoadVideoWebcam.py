import cv2

#cap = cv2.VideoCapture("images/red_panda_snow.mp4")
#                        DirectShow
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    print('Size',frame.shape)  # Size (480, 640, 3)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(40)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()