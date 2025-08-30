import cv2 as cv
import numpy as np

img = cv.imread('E:/UAS/3.png')
#cv.imshow('3', img)

#converting BGR to grayscale
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('grayimg', grayimg)

#converting BGR to HSV
hsvimg=cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('hsvimg', hsvimg)

#we can also split the image into the 3 channels(blue, green and red)
b, g, r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

cv.waitKey(0)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#we can merge the channels to get back the original image
mergeimg = cv.merge([b,g,r])
cv.imshow('merged', mergeimg)
cv.waitKey(0)

#if we want to see the channels as actually bgr instead of grayscale, we can merge it with blank in the BGR format

