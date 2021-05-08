import cv2

road_org = cv2.imread('images/road.jpg')
car_org = cv2.imread('images/car.jpg')

car_gray = cv2.cvtColor(car_org, cv2.COLOR_BGR2GRAY)

# mask=255 Hintergrund/road  mask=0 car
ret, mask = cv2.threshold(car_gray, 240, 255, cv2.THRESH_BINARY)
# mask_inv=255 car,  mask_inv=0 Hintergrund/road
mask_inv = cv2.bitwise_not(mask)

# road im Hintergrund
road = cv2.bitwise_and(road_org, road_org, mask=mask)
car = cv2.bitwise_and(car_org, car_org, mask=mask_inv)

result = cv2.bitwise_or(road,car)
#result = cv2.add(road,car)

cv2.imshow('road_org', road_org)
cv2.imshow('car_org', car_org)
cv2.imshow('road background',road)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('car no background',car)
cv2.imshow('car_on_road',result)
cv2.waitKey(0)
cv2.destroyAllWindows()