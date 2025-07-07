import numpy as np
# Replace nan values with average of columns....
arr = np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
col_mean = np.nanmean(arr,axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col_mean, inds[1])
print(arr)