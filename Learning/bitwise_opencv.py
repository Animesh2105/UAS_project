import cv2 as cv
import numpy as np

blank = np.zeros((500,500), dtype='uint8')
#copying the blank file and creating a rectangle on it
rectangle = cv.rectangle(blank.copy(), (40,40), (460,460), 255, -1)

#copying the blank file again and creating a circle on it
circle = cv.circle(blank.copy(), (250,250), 240, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

#bitwise and
bitwise_and= cv.bitwise_and(rectangle, circle)
cv.imshow('and', bitwise_and)

#bitwise or
bitwise_or=cv.bitwise_or(rectangle, circle)
cv.imshow('or', bitwise_or)

#bitwise xor - only returns non intersecting regions
#bitwise not - single image, returns region not in the image


cv.waitKey(0)