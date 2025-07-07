import numpy as np
arr1 = np.array([3,4])
arr2 = np.array([1,0])
#Avg of numpy arrays
avg = (arr1+arr2)/2
print("Average of Numpy arrays:\n",avg)


#  Mean , Median, Mode of two numpy 2d arrays....
arr_1 = np.array([[3,4],[5,6]])
arr_2 = np.array([[5,6],[3,2]])
# Mean
Mean = (arr_1+arr_2)/2
print(Mean)
# Median
Median = np.median([arr_1,arr_2])
print(Median)
# Mode
combined_flatten = np.concatenate((arr_1.flatten(), arr_2.flatten()))
unique, counts = np.unique(combined_flatten, return_counts=True)
mode_val = unique[np.argmax(counts)]
print(mode_val)