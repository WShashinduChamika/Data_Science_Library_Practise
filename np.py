import numpy as np

print(np.__version__)

np_array = np.array([1,2,3,4])

print(np_array)


# Multi dimentional arrays

array_2D = np.array([[1,2,3], [4,5,6]])
print(array_2D)

array_3D = np.array([[[1,2],[3,4]], [[5,6], [7,8]]])
print(array_3D)

# Use of ndim for gaining the dimention type
print(np_array.ndim)
print(array_2D.ndim)


#Use of ndmin for change the dimention as needed
np_array2 = np.array([1,2,3,4], ndmin=4)
print(np_array2.ndim)