import numpy as np
# 1. Create a rank 2(2D) array
arr = np.array([[11,12,13,14],[15,16,17,18]])

print(arr)

# 2. Create an array with 4 rows and 3 columns of zeros
A = np.zeros((4,3))

print(A)

#3. Create an array of ones that has 3 rows and 4 columns

B = np.ones((3,4))

print(B)

#4.  Create an array containing integers 4 to 13 inclusive. Your results should look as below:

range1 = np.arange(4,14)
print(range1)

#5. Create an array containing [0., 1.5, 3., 4.5]

range2 = np.linspace(0,4.5,4)

print(range2)

#Create a 2 by 2 array containing '4' in each position. Your results should look like this: [[4 4],[4 4]]
range3 = np.full((2,2),4)
print(range3)

#Create 2 matrices:
#Identity matrix of size 4
range4 = np.eye(4)
print(range4)

#Diagonal matrix with [10,12] as the diagonals

range5 = np.diag([10,12])
print(range5)

#Create a 3 by 3 array with random floats in [0, 10]
range6 = np.random.random((3,3)*10)
print(range6)








