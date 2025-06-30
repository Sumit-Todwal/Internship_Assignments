import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
reverse = array.flatten()[::-1]
arr = reverse.reshape(3,3)
print(arr)