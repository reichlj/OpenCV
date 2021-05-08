import cv2 as cv

def capture_and_display_video():
    cap = cv.VideoCapture(0)      # first camera - 0 is a device index
    # cap captures one frame after the other
    if not cap.isOpened(): # check if cap is initialized correctly
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:   # if frame is read correctly ret is True otherwise False
            print("Can't receive frame (stream end?). Exiting ...")
            break
        print('frame.shape',frame.shape)
        # frame is a numpy array, uint8 with 3 channels  (height=480,width=640,3)
        print('Width', cap.get(cv.CAP_PROP_FRAME_WIDTH))    # 640
        print('Height', cap.get(cv.CAP_PROP_FRAME_HEIGHT))  # 480
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # gray is a numpy array, uint8 (height=480,width=640)
        gray[470:480,600:640]=255
        cv.imshow('frame', gray)
        if cv.waitKey(10) == ord('q'):
            break

    cap.release()  # release WebCam
    cv.destroyAllWindows()

def play_video_file():
    cap = cv.VideoCapture('output_640_480.avi') # get frames from file instead of camera
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(25) == ord('q'): # wait 25 ms to display frame
            break

    cap.release()
    cv.destroyAllWindows()

def capture_and_store_video():
    cap = cv.VideoCapture(0)
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv.VideoWriter_fourcc('X','V','I','D') # video codec
    #                                          fps  (width, height)
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv.flip(frame, 0)
        # write the flipped frame
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    capture_and_display_video()
    play_video_file()
    #capture_and_store_video()