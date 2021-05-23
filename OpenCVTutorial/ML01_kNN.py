import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
# Label each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0,2,(25,)).astype(np.float32)
# Take Red neighbours and plot them
red = trainData[responses==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')
# Take Blue neighbours and plot them
blue = trainData[responses==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

#newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
newcomer = np.random.randint(0,100,(3,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

# Static method to create empty KNearest classifier.
# It should be then trained using StatModel::train method.
knn = cv.ml.KNearest_create()
#                    each training sample is a row of samples
#                                      vector of responses associated with the training sample
knn.train(trainData, cv.ml.ROW_SAMPLE, responses)
ret, results, neighbours ,dist = knn.findNearest(newcomer, 3)
# result:  [ [0.], [0.], [0.] ]  i.e. the 3 newcomers are labeled red
# neighbours:  [ [0. 0. 1.], [1. 0. 0.], [0. 0. 0.] ]  nearest neighbors are labeled
# distance:  [ [ 101.  225.  680.], [ 272. 1153. 1394.], [  89.  720. 1073.] ]
print( "result:  {}\n".format(results) )
print( "neighbours:  {}\n".format(neighbours) )
print( "distance:  {}\n".format(dist) )
plt.show()