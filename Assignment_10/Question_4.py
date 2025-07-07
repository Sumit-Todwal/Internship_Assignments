import numpy as np
# Replace neg values with Zeroes.....
arr = np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
arr[arr < 0] = 0
print(arr)