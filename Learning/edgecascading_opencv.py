import cv2 as cv
def imgshow(x):
    cv.imshow('x', x)
    cv.waitKey(0) 
#edge cascading - this helps us find the edges in a photograph
img = cv.imread('E:/UAS/1.png')
edgeimg = cv.Canny(img, 120, 120)
imgshow(edgeimg)
#blur and grascale are also imp functions
resizeimg = cv.resize(img, (500,500))
imgshow(resizeimg)
croppedimg = img[100:200, 200:300]
imgshow(croppedimg)