import numpy as np
# Replacing Nan with Zeroes...
arr = np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
result = np.nan_to_num(arr)
print(result)
# Interchange three columns and three rows.....
arr_new = np.transpose(result)
print(arr_new)