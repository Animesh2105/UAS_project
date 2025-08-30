import cv2 as cv
#thresholding is a way of binarizing the image, giving pixels having intensity above a certain threshold
img = cv.imread('E:/UAS/6.png')
cv.imshow('6', img)
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayimg', grayimg)

#Simple thresholding
threshold, thresh = cv.threshold(grayimg, 150, 255, cv.THRESH_BINARY)   #if a pixel has intensity above 150, it sets it to 255, otherwise 0
cv.imshow('simplethresh', thresh)
threshold, thresh_inv = cv.threshold(grayimg, 150, 255, cv.THRESH_BINARY_INV) #this inverts the previous thresholded image
cv.imshow('simplethresh_inv', thresh_inv)

#Adaptive thresholding
threshold_adaptive = cv.adaptiveThreshold(grayimg, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) #this sets the threshold value wrt to the pixels surrounding it
cv.imshow('adaptivethresh', threshold_adaptive)

cv.waitKey(0)