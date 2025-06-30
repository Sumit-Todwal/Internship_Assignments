import numpy as np
import pandas as pd

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
reverse = arr.flatten()[::-1]
print(reverse)
reshape = reverse.reshape((3,3))
print(reshape)