import cv2

img = cv2.imread('images/the_book_thief.jpg',cv2.IMREAD_GRAYSCALE)
index = 0
if index == 0: # patented, free since OPenCV 4.3
    # sift - scale invariant feature transform
    # extracting keypoints and computing descriptors using the SIFT
    sift = cv2.xfeatures2d.SIFT_create()
    #kp = sift.detect(img,None)
    kp,descriptors = sift.detectAndCompute(img,None)
elif index == 1: # patented
    # surf - Class for extracting Speeded Up Robust Features from an image
    surf = cv2.xfeatures2d.SURF_create()
    kp,descriptors = surf.detectAndCompute(img,None)
elif index == 2: # for free
    # ORB - oriented BRIEF - keypoint detector and descriptor extractor
    orb = cv2.ORB_create(nfeatures=1500)
    kp,descriptors = orb.detectAndCompute(img,None)

img = cv2.drawKeypoints(img,kp,None)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()