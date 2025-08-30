import numpy as np
arr1=np.array([1,2,3,4,5])      #array with rank 1
arr2=np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])     #array with rank 2
print(arr1[:3:2])       #prints from beginning to index 2, taking 2 steps at a time, using the format start:stop:step
print(arr2[0:2, 1:3])   #prints row 0-1 and columns 1-2
print(arr1+1)
var = "animesh"
#fromiter lets us create array from an iterable, we specify the return data type as unicode string of length 2 and only count the first 3 characters
arr3=np.fromiter(var, dtype='U2', count = 3)
print(arr3)
var2 = (x*x for x in range(1,5))
#in this example, we use list comprehension
arr4 = np.fromiter(var2, dtype=float)
print(arr4)
#we can also use other commands to create identity, diagonal and random matrices
arr5=arr2.reshape(5,4)
print(arr5)
