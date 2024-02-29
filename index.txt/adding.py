import numpy as np

#ADDING ELEMENTS
#Use this array for the following practice:

myArray = np.array([[11,12,13], [14,15,16], [17,18,19]])

#1. Add a new row of elements containing 20, 21 and 22

new_row = np.array([20,21,22])
updated_array = np.vstack((myArray,new_row))
print(updated_array)

#2. Add a new column of elements containing 30, 40 and 50
new_column = np.array([[30],[40],[50]])

updated_column_array = np.hstack((myArray,new_column))
print(updated_column_array)