import numpy as np
# Move axes to new positions....
arr = np.arange(24).reshape(2,3,4)
print(arr)
print(arr.shape)
movedaxes = np.moveaxis(arr,0,2)
print(movedaxes)
print(movedaxes.shape)

# In moveaxis() their is no swapping of axis's 
    #  instead place that axis at that position and relative
    # order of axis remains the same....