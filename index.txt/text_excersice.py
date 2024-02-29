import numpy as np
#Replace all odd numbers in the given array with -1
exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
exercise_1[exercise_1 % 2 == 1] = -1
print(exercise_1)


#Convert a 1-D array into a 2-D array with 3 rows
exercise_2 = np.array([0,1,2,3,4,5,6,7,8])
## Convert exercise_2 into a 2-D array with 3 rows
exercise_2_reshaped = exercise_2.reshape(3, -1)
print(exercise_2_reshaped)

#Add 202 to all the values in given array

exercise_3 = np.arange(4).reshape(2,-1)
# Add 202 to all the values in exercise_3
exercise_3_updated = exercise_3 + 202
print(exercise_3_updated)