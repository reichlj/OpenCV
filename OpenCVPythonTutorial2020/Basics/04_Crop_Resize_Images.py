import cv2

path = "../Resources/chess.jpg"
img  = cv2.imread(path)
print(img.shape)

width ,height = 1000 , 1000
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)

imgCropped = img[200:400,260:450]
print(imgCropped.shape)
imCropResize  = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
print(imCropResize.shape)

cv2.imshow("Road",img)
cv2.imshow("Road Resized",imgResize)
cv2.imshow("Roa",imgCropped)
cv2.imshow("Road Cropped Resized",imCropResize)
cv2.waitKey(0)
cv2.destroyAllWindows()

