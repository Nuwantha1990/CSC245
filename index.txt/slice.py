import numpy as np

# Slice

myArray = np.array([[11,12,13], [14,15,16], [17,18,19]])
#a. Get a subarray of the first row and first 2 columns. Your results should look like this:
#[11 12]

print(myArray[0,0:2])

#b. Change all elements in 1st and second row to 0. Your results should look like this:
myArray[0:2] = 0
print(myArray)

#2. Create an array that contains [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] and reverse the order.

myArr = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
reversed_myArr = myArr[::-1]
print(reversed_myArr)

#Use this array for the following practice:
mynewArray = np.array([[11,12,13], [14,15,16]])

#Reshape the array to an array with 3 rows. Your results should look like this:
#[11 12]
#[13 14]
#[15 16]]

reshaped_array = mynewArray.reshape(3,2)
print(reshaped_array)




