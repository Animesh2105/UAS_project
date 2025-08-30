import cv2 as cv
import numpy as np

img = cv.imread('E:/UAS/4.png')
cv.imshow('4', img)

#we create a 'mask' to put over the image, in this case a circle over the black screen, needs to be of the same dimensions as the image
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

#we use the bitwise and operator to "mask" the image
maskedimg = cv.bitwise_and(img,img, mask=mask)
cv.imshow('maskedimg', maskedimg)

cv.waitKey(0)
