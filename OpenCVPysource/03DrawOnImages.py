import cv2
import numpy as np

image  = cv2.imread("images/red_panda.jpg")
shape = image.shape
print(shape)
blue = (255,0,0)
red = (0,0,255)
green = (0,255,0)
violet = (180,0,180)
yellow = (0,180,180)
white = (255,255,255)
#                x  y
cv2.line(image,(50,30), (450,35),blue,thickness=5)
cv2.circle(image,(238,205),23,red,-1)
cv2.rectangle(image,(50,60),(450,95),green,thickness=-1)
cv2.ellipse(image,(250,150),(80,20),angle=90,startAngle=0,endAngle=330,color=violet,thickness=-1)

points = np.array([[[140,230],[380,230],[320,240],[250,280]]],np.int32)
cv2.polylines(image,[points],True,yellow,thickness=3)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,'Panda',(20,180),font,3,white)
cv2.imshow("red panda",image)
cv2.waitKey(0)
cv2.destroyAllWindows()