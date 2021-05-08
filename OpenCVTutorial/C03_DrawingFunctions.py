import numpy as np
import cv2 as cv

def next_image():
   print('Press q within image to close display')
   z = 0
   while z != ord('q'):  # wait until 'q' is pressed
      z = cv.waitKey(0)  # 0 means wait forever, 5 means wait 5 ms
   cv.destroyAllWindows()

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511//2,511),(255,0,0),5)

#          (x_top_left=384, y_top_left=0)
#              (x_bottom_right=510, y_bottom_right=128)
#                                   color    thickness -1 means fill
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.circle(img,(447,63), 63, (0,0,255), cv.FILLED)

#              x_center,y_center
#                      major, minor axis length
#                                 angle of rotation
#                                    start angle
#                                       stop angle
#                                           color
#                                               thickness
cv.ellipse(img,(256,256),(100,50),10, 0, 130,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts1 = np.array([[30,15],[60,130],[60,120],[60,110]], np.int32)
#pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts,pts1],True,(0,255,255))

font = cv.FONT_HERSHEY_SIMPLEX
#                      bottom left corner
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('line',img)
next_image()
