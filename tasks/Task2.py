#the code works as expected, however there are still some problems with image and colour detection which couldnt be tuned out due to time constraints
#the program does not seem to work for 1.png, likely due it not being able to scan the rescue pad colors. it works for all other files.
import cv2 as cv
import numpy as np

img = cv.imread('enter filename here')
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsvimg = cv.cvtColor(img, cv.COLOR_BGR2HSV)
blurimg = cv.bilateralFilter(grayimg, 9, 75, 75)
#Using Canny edge detection on a blurred and grayscale image
edgeimg = cv.Canny(blurimg, 50, 150)

#defining a function to the get the location of the casualties and the rescue pads
def get_location(contour):
    M = cv.moments(contour)
    if M["m00"] == 0:  # avoids
        return (0, 0)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    return (cx, cy)

def distance(c1, c2):
    return np.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)

def getCasualtydata(n):
    for padindex, details in pads.items():
      if details["capacity"]==n:
        i = 0
        for id in details["assigned"]:
            print(f"{casualties[id]["age"], casualties[id]["emergency"]}")
            i+=1
        print("Total casualties assigned: ", i)
    print('\n')
    


#we use findContours to detect the external edges of the shapes in the image
contours, hierarchies = cv.findContours(edgeimg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

casualty_id = 1
casualties = {}
pad_id = 1
pads = {}

for contour in contours:
     area = cv.contourArea(contour)
     if area < 20:
        continue
     #this part was a bit tricky, approxPolyDp lets us approximate a set of contours as a polygon, needs an epsilon (an error value, basically)
     #some help from the internet was used to find what a good epsilon value is supposed to be
     location = get_location(contour)
     perimeter = cv.arcLength(contour, True)
     shape = cv.approxPolyDP(contour, 0.035*perimeter, True)
     edges = len(shape)
     mask = np.zeros(grayimg.shape, dtype = 'uint8')
     cv.drawContours(mask, [contour], -1, 255, -1)
     H, S, V, alpha = cv.mean(hsvimg, mask = mask)    #we extract the hsv values for segmentation based on emergency level
     if edges == 3:
        age = 2   #elderly
     elif edges == 4:
        age =  1  #adult
     elif edges ==10: 
        age = 3   #children
     else:
      #here we segment and store the data for the rescue pads
      if 90 <= H <= 130:       # blue
            capacity = 4
      elif 140 <= H <= 170:    # pink
           capacity = 3
      elif S < 40 and V > 180: # grey
            capacity = 2
      pads[pad_id]={
          "capacity": capacity,
          "location": location
      }
      pad_id+=1
      continue
     #now we use the hsv values to assign emergency levels to the casualties, and designated capacities to the rescue pads
     if edges != 8:
         if 25<H<50 and S>140:
            emergency = 2   #moderate
         elif H<50 and S<85:
            emergency = 3   #severe (this was a bit frustrating, since the color was very washed out)
         elif 45<H<70 and S<140:
            emergency = 1   #safe
         else:
            emergency = 0
         casualties[casualty_id] = {
        "age": age,
        "emergency": emergency,
        "location": location,
        "priority score": age*emergency,
         "distances" : {},
         "scores" : {},
         "best pad": {}
       }
     casualty_id+=1

#All the data scanning, segmentation and storage is done
for index in casualties:
    p1 = (casualties[index]["location"])
    for padindex in pads:
        p2 = (pads[padindex]["location"])
        dist = distance(p1, p2)     #get the location of both the casualty and pads to calculate the distance
        casualties[index]["distances"][padindex]=dist
        score = casualties[index]["priority score"]*100-dist
        casualties[index]["scores"][padindex]=score
        pads[padindex]["assigned"]=[]
    
#we now have both the priority score and the distance from each rescue pad stored along with the id of the casualty
#we use the formula priority score*100 - distance to calculate the final score
sorted_casualties = sorted(
    casualties.items(),
    key=lambda item: max(item[1]["scores"].values()),    #this sorts casualties in descending order of their scores
    reverse=True
)
for index, details in sorted_casualties:
    sorted_scores = sorted(details["scores"].items(), key=lambda x: x[1], reverse=True)   #this ranks the casualties best pad option in order
    for padindex, score in sorted_scores:
        if len(pads[padindex]["assigned"]) < pads[padindex]["capacity"]:
            pads[padindex]["assigned"].append(index)    
            details["best pad"] = padindex           
            break

#the casualties have now been assigned pads on the basis of emergency and distance
#outputting the data in the required format
print("Casualty details for blue pad (capacity = 4)")
getCasualtydata(4)

print("Casualty details for pink pad (capacity=3)")
getCasualtydata(3)

print("Casualty data for grey pad (capacity =2)")
getCasualtydata(2)