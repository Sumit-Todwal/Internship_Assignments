import numpy as np
arr1 = np.array([[[1,-2,3],[-1,3,-1],[2,-5,5]]])
arr2 = np.array([9,-6,17])
arr3 = np.linalg.solve(arr1,arr2)
print(arr3)
# Using inverse matrix method
arr1_inv = np.linalg.inv(arr1)
res = np.dot(arr1_inv,arr2)
print(res)