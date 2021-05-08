import cv2
import numpy as np

#     hmin, smin, bmin  hmax, smax, bmax
# myColors = [[  5,107,  0,   19,255,255],  # orange
#             [133, 56,  0,  159,156,255],   # purple
#             [ 57, 76,  0,  100,255,255],
#             [ 90, 48,  0,  118,255,255]]

myColors = [[ 26, 18,  0,   29,255,255],  # MarkerGelb
            [106, 35, 21,  135,255,255],  # MarkerViolett
            [  0, 89, 21,    6,255,255]]  # Stiftrot
#                   B    G    R
myColorValues = [[  0, 255, 255],     # Gelb
                 [255,   0, 127],     # Violett
                 [  0,   0, 255] ]    # Rot

myPoints =  []  ## [x , y , colorId ]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints=[]
    for count, color in enumerate(myColors):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask,count)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img,count):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    nbr_of_areas = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>600:
            nbr_of_areas = nbr_of_areas +1
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    print('count',count,'Nbr of Contours',len(contours),'nbr_of_areas',nbr_of_areas)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # 3
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 4
cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)    # 10

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
