import numpy as np

#INSERTING ELEMENTS
myArray = np.zeros((2,2))
print(myArray, "\n")


#Add 1 column of 1 to this array:

myArray_1 = np.append(myArray,np.ones((2,1)),axis=1)
print(myArray_1, "\n")

#Add 2 rows of 2 to the answer from part 1
myArray_2 = np.append(myArray_1,[[2,2,2],[2,2,2]],axis=0)
print(myArray_2, "\n")

#Remove the last column
myArray_3 = np.delete(myArray_2,2,axis=1)
print(myArray_3, "\n")
#Remove the last row
myArray_4 = np.delete(myArray_3,3,axis=0)
print(myArray_4, "\n")