import cv2 as cv

img = cv.imread('E:/UAS/4.png')
cv.imshow('4', img)

#average blur(this type of blurring gives the pixel in a nxn kernel the average of the intensity of its surrounding pixels)
avgblur = cv.blur(img, (5,5))
cv.imshow('avgblur', avgblur)

#gaussian blur(kind of like average, but takes weighted means)
gaussblur = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('gaussblur', gaussblur)

#median blur (effective in reducing noise in the image, use small kernel sizes)
medianblur = cv.medianBlur(img, 3)
cv.imshow('medianblur', medianblur)

#bilateral blur
cv.waitKey(0)

