import numpy as np
#Remove the elements from the middle column of this array:
myArray = np.matrix([[1, 2, 3], [4, 5, 6], [9, 8, 7]])
myArray_new = np.delete(myArray,1,axis=1)
print(myArray_new)