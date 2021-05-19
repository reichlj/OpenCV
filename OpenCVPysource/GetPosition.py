import cv2

point1 = None
point2 = None
drawing = False

def mouse_drawing(event, x, y, flags, params):
    global point1, point2, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = (x, y)
            point2 = None
        else:
            drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            point2 = (x, y)

img_org = cv2.imread('videos/flasche_first.jpg')

cv2.namedWindow('Image')
cv2.setMouseCallback('Image',mouse_drawing)

while True:
    img = img_org.copy()
    if point1 and point2:
        cv2.rectangle(img,point1,point2,(0,0,255),1)
        if drawing:
            print('Point1',point1,'  Point2',point2)
            print('  Width={0:d} Height={1:d}'.format(point2[0]-point1[0],point2[1]-point1[1]))
    cv2.imshow('Image',img)
    key = cv2.waitKey(100)
    if key == 27:
        break

cv2.destroyAllWindows()