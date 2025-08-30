import cv2 as cv
import numpy as np

img = cv.imread('E:/UAS/2.png')
edgeimg=cv.Canny(img, 125, 175)
#opencv has contour detection using the following statement(needs a binary image, not a 3 channel)
contours, hierarchies = cv.findContours(edgeimg, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#RETR_LIST returns all the contours, use RETR_EXTERNAL for outer contours 

print(len(contours))    #contours returns a list, so this returns the number of contours in the image

blank = np.zeros(img.shape, dtype='uint8')  #this prints a blank image of the same dimensions as img

#we can use this blank image to write our contours on
cv.drawContours(blank, contours, -1, (255,255,255), 1)
cv.imshow('contours', blank)
cv.waitKey(0)