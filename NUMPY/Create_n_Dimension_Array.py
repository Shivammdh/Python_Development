import numpy as np
n=int(input())
arr = np.array([1, 2, 3, 4], ndmin=n)

print(arr)
print('number of dimensions :', arr.ndim)