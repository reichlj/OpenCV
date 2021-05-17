import cv2

cap = cv2.VideoCapture("images/red_panda_snow.mp4")
#cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    cv2.imshow("frame", frame)

    key = cv2.waitKey(40)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()