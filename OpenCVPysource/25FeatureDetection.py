import cv2

# KeyPoint
# The keypoint is characterized by the 2D position, scale (proportional to the diameter
# of the neighborhood that needs to be taken into account), orientation and some other
# parameters. The keypoint neighborhood is then analyzed by another algorithm that builds
# a descriptor (usually represented as a feature vector). The keypoints representing the
# same object in different images can then be matched using KDTree or another method.

#float 	angle
#int class_id  	object class (if the keypoints need to be clustered by an object they belong to) More...
#int octave 	octave (pyramid layer) from which the keypoint has been extracted More...
#Point2f pt 	coordinates of the keypoints More...
#float response response by which the most strong keypoints have been selected. Can be used for the further sorting or subsampling More...
#float size     diameter of the meaningful keypoint neighborhood More...

img = cv2.imread('images/the_book_thief.jpg',cv2.IMREAD_GRAYSCALE)
index = 0
if index == 0: # patented, free since OPenCV 4.3
    # sift - scale invariant feature transform
    # extracting keypoints and computing descriptors using the SIFT
    sift = cv2.SIFT_create()
    #kp = sift.detect(img,None)
    kp,descriptors = sift.detectAndCompute(img,None)
elif index == 1:
    # surf - Class for extracting Speeded Up Robust Features from an image
    surf = cv2.SURF_create()
    kp,descriptors = surf.detectAndCompute(img,None)
elif index == 2: # for free
    # ORB - oriented BRIEF - keypoint detector and descriptor extractor
    orb = cv2.ORB_create(nfeatures=1500)
    kp,descriptors = orb.detectAndCompute(img,None)

img = cv2.drawKeypoints(img,kp,None)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()