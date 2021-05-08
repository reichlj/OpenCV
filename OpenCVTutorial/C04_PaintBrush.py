import cv2 as cv
import numpy as np

img = None

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

def show_events():
    events = [i for i in dir(cv) if 'EVENT' in i]
    for ev in events:
       print( ev )

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)

def create_circles():
    global img
    # Create a black image, a window and bind the function to window
    img = np.zeros((512,512,3), np.uint8)
    cv.namedWindow('image') # create a window and load image to it later
    cv.setMouseCallback('image', draw_circle)
    while True:
        cv.imshow('image', img)
        print('XXX')
        if cv.waitKey(2) & 0xFF == 27:
            break
    cv.destroyAllWindows()

def draw_circle_and_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),3)
            else:
                cv.circle(img,(x,y),10,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),3)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

def create_circles_and_rectangles():
    global img, mode
    img = np.zeros((512,512,3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image',draw_circle_and_rectangle)
    while True:
        cv.imshow('image',img)
        k = cv.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break
    cv.destroyAllWindows()


if __name__ == '__main__':
    #show_events()
    #create_circles()
    create_circles_and_rectangles()