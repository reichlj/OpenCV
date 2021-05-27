import cv2

cap = cv2.VideoCapture("images/red_panda_snow.mp4")
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("images/flipped_red_panda.avi", fourcc, 25, (640, 360))

while True:
    ret, frame = cap.read()
    frame2 = cv2.flip(frame, 1)

    cv2.imshow("Flipped Frame", frame2)
    cv2.imshow("Original Frame", frame)

    out.write(frame2)

    key = cv2.waitKey(25)
    if key == 27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()