import cv2 as cv
import numpy as np
def imgshow(x):
    cv.imshow('x', x)
    cv.waitKey(0)    
img = cv.imread('E:/UAS/1.png')
cv.imshow('1', img)
cv.waitKey(0)
#this creates a blank image of dimensions 500*500 (uint8 is the dtype for an image)
blank = np.zeros((500,500, 3), dtype ='uint8')
#this prints the entire image blue
blank[:]=0,0,255
#this prints a section of the image red
blank[100:200, 200:300]=255,0,0
imgshow(blank)
#this prints a rectangle in the image from pt1 to pt2, you can specify the border thickness or just fill it completely
cv.rectangle(blank, (0,0), (200,300), (0,255,0), thickness=cv.FILLED) #(img, pt1, pt2, colour, thickness)
imgshow(blank)
#this prints a circle in the format (img, center, radius, colour, thickness)
cv.circle(blank, (250,250), 40, (0,0,0), thickness=4)
imgshow(blank)
#You can also use cv.line similarly
#You can put text into the image using cv.putText(img, string, position, font face, scale, colour, thickness)
