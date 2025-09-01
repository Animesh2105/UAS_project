# 🚁 UAS-DTU Round 2 Task – Search & Rescue
📌 Overview  
This project uses computer vision (OpenCV + Python) to:  
-Detect casualties in an input image (classified by age & emergency level).  
-Detect rescue pads and their capacities.  
-Assign casualties to the nearest available rescue pads based on distance and pad capacity.  

## Task 1
The main goal of this task is to process the image and segment images into ocean and land (using masking in HSV colour spaces) and then overlay a unique colour to for clearer differentiation.

## Task 2
For this task, the emergency level, age, and the distance from the rescue pads was accessed and stored for each casualty. Then, the best rescue camp for each was assigned on the basis of a final score calculated by the amalgamation of the Priority score and distance where the priority score is Priority(casualty*emergency). In case of a similar priority score , a casualty with higher emergency score was given importance.

## Task 3
For this task, we have to calculate thhe total priority of each of the camps saved in a list and the average priority of the image (rescue ratio of priority Pr) , calculated by summing the priorities of the camps and averaging over the number of casualties.
