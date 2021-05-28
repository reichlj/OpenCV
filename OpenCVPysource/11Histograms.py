import cv2

import matplotlib.pyplot as plt
if 1==1:
    img= cv2.imread('images/sea.jpg')
    img= cv2.imread('images/sea_beach.jpg')
    cv2.imshow('img',img)
    b,g,r= cv2.split(img)
    cv2.imshow('b',b)
    cv2.imshow('g',g)
    cv2.imshow('r',r)
    plt.hist(b.ravel(),256,[0,256])
    plt.hist(g.ravel(),256,[0,256])
    plt.hist(r.ravel(),256,[0,256])
else:
    img =  np.zeros((100,100),np.uint8)
    cv2.rectangle(img,(0,50),(100,100),255,-1)
    cv2.circle(img,(50,50),25,127,thickness=-1)
    cv2.imshow('img',img)
    plt.hist(img.ravel(),bins=256,range=[0,256])

plt.show()
key=cv2.waitKey(0)
cv2.destroyAllWindows()