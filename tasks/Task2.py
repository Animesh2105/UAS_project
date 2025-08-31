import cv2 as cv
import numpy as np

img = cv.imread('E:/UAS/3.png')
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurimg = cv.bilateralFilter(grayimg, 9, 75, 75)
#Using Canny edge detection on a blurred and grayscale image
edgeimg = cv.Canny(blurimg, 50, 150)

#we use findContours to detect the external edges of the shapes in the image
contours, hierarchies = cv.findContours(edgeimg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
     area = cv.contourArea(contour)
     if area < 20:
        continue
     #this part was a bit tricky, approxPolyDp lets us approximate a set of contours as a polygon, needs an epsilon (an error value, basically)
     #some help from the internet was used to find what a good epsilon value is supposed to be
     perimeter = cv.arcLength(contour, True)
     shape = cv.approxPolyDP(contour, 0.035*perimeter, True)
     edges = len(shape)
     if edges == 3:
        age = "elderly"
     elif edges == 4:
        age =  "adult"
     elif edges != 8: #this is a bit of frankencode, cant get approxpolydp to always recognise stars without breaking everything else and circles come up as 8 edges so..
        age = "children"
     else:
        continue
     #now that we have differentiated the shape of the objects, we move to segmenting them by colour
     mask = np.zeros(grayimg.shape, dtype = 'uint8')
     cv.drawContours(mask, [contour], -1, 255, -1)
     B, G, R, alpha = cv.mean(img, mask = mask)    #this returns the mean bgr values of that specific shape we mask
     #now we use the bgr values to assign emergency levels to the victims, and designated capacities to the rescue pads
     if edges != 8:
        if R > 150 and G > 150 and B < 100:
            emergency = "moderate"
        elif R > 150 and G < 100 and B < 100:
            emergency = "severe"
        elif G > 150 and R < 100 and B < 100:
            emergency = "safe"
     elif edges == 8:   #since circles show up as 8 edges
          if R > 180 and B > 180 and G < 150:
            capacity = 3
          elif B > 150 and R < 100 and G < 100:
            capacity = 4
          elif abs(R - G) < 20 and abs(G - B) < 20 and 80 < R < 200:
            capacity = 2
      


        
     



        
     

