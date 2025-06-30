import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
arr3 = arr1.reshape(1,4)
result = np.concatenate((arr2,arr3),axis=0)
print(result)