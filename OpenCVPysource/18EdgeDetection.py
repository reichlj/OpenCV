import cv2

img = cv2.imread("images/white_panda.jpg",cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img,(11,11),0)
#  −1  0  1
#  −2  0  2
#  −1  0  1
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
#  −1  -2 -1
#   0   0  0
#   1   2  1
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)

#   0   1  0
#   1  -4  1
#   0   1  0
laplacian = cv2.Laplacian(img,cv2.CV_64F,ksize=5)

canny = cv2.Canny(img,100,150)

cv2.imshow("WhitePanda",img)
cv2.imshow("Sobelx",sobelx)
cv2.imshow("Sobely",sobely)
cv2.imshow("Laplacian",laplacian)
cv2.imshow("Canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
