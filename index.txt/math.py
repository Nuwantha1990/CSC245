import numpy as np
#Use this array for the following practice:

myArray = np.arange(10)

#1. Find the square of every number in array

squared_array = myArray **2
print(squared_array)

#2. Find the square root of every number in array
squaredroot_array = np.sqrt(myArray)
print(squaredroot_array)

#3. Multiply the square of each number in array with its respective square root
multiply_array = squared_array * squaredroot_array
print(multiply_array)
