import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
# max_value
max_value = array.max()
print(max_value)

#min value
min_value = array.min()
print(min_value)

# No. of rows and columns
rows, column = np.shape(array)
print("No. of rows",rows)
print("No. of column",column)

for element in array:
    print(element)

# For any specific element..
# print(array[element_row][element_column])

# sum of values using loop
total = 0
for element in array:
    total += element.sum()
print(total)

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[1,2,3]])
# Adding...
print(arr1 + arr2)
# Subtracting...
print(arr1 - arr2)
# Multiplying..
print(arr1 * arr2)
# Dividing...
print(arr1/arr2)