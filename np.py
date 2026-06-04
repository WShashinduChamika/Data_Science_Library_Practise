import numpy as np

# print(np.__version__)

# np_array = np.array([1,2,3,4])

# print(np_array)


# # Multi dimentional arrays

# array_2D = np.array([[1,2,3], [4,5,6]])
# print(array_2D)

# array_3D = np.array([[[1,2],[3,4]], [[5,6], [7,8]]])
# print(array_3D)

# # Use of ndim for gaining the dimention type
# print(np_array.ndim)
# print(array_2D.ndim)


# #Use of ndmin for change the dimention as needed
# np_array2 = np.array([1,2,3,4], ndmin=4)
# print(np_array2.ndim)

# # Array indexing
# arr = np.array([1,2,3])
# print(arr[1])

# # Multi dimenational array indexing
# arr_2D = np.array([[1,2,3], [5,6,7], [7,8,9]])
# print(arr_2D[0,1])

# arr_3D =  np.array([[[1,2],[2,3]],[[4,5],[6,7]]])
# print(arr_3D[0,1,0])

# # Negative indexing
# new_arr = np.array([1,2,3,4,5])
# print(new_arr[-3])

# # Array Slicing
# arr = np.array([1,2,3,4,5,6])
# print(arr)

# #x[start:end]
# print(arr[1:4])

# print(arr[-5:-1])

# print(arr[2:])

# print(arr[:3])

# #x[start:end:step]
# print(arr[1::2])

# arr2D = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(arr2D)
# print(arr2D[:1,1:])


# arr = np.array([1, 2], dtype='f')
# print(arr)
# print(arr.dtype)

# arr2 = np.array(['Python', 'Java'])
# print(arr2)
# print(arr2.dtype)

# arr3 = np.array([1.2,2,3,4])
# print(arr3)
# print(arr3.dtype)

# converated_arr = arr3.astype(bool)
# print(converated_arr)
# print(converated_arr.dtype)

# arr1 = np.array([1,2,3,4])
# arr2 = arr1.copy()
# arr3 = arr1.view()

# arr1[0] = 5

# print(arr1)
# print(arr2)
# print(arr3)

# print(arr2.base)
# print(arr3.base)

# #Iterating
# arr = np.array([1,2,3,4])

# for i in arr:
#     print(i)
# print()


# arr_2D = np.array([[1,2,3], [4,5,6]])

# for i in arr_2D:
#     for j in i:
#         print(j)
# print()


# for i in np.nditer(arr_2D[:,::2]):
#     print(i)
# print()

# for i,j in np.ndenumerate(arr_2D):
#     print(i,j)


# # Shape and Reshape

# # Shape
# arr_2D = np.array([[1,2,3], [4,5,6]])

# print(arr_2D)
# print(arr_2D.shape)
# print()

# arr_3D = np.array([[[1,2,3], [4,5,6]], [[7,8,3], [1,7,6]], [[7,8,3], [1,7,6]]])

# print(arr_3D)
# print(arr_3D.shape)
# print()

# arr_5D = np.array([1,2,3,4,5], ndmin=5)
# print(arr_5D)
# print(arr_5D.shape)
# print()

# # Reshape
# arr = np.array([1,2,3,4,5,6,7,8,9])

# new_arr = arr.reshape(1,9)
# print(new_arr)

# arr2 = np.array([1,2,3,4,5,6,7,8])

# new_arr2 = arr2.reshape(2,2,2)
# print(new_arr2)

# arr_2D = np.array([[1,2,3], [4,5,6]])
# new_arr3 = arr_2D.reshape(-1)
# print(new_arr3)

# arr = np.array([[1,2], [3,4]])

# x = np.where(arr==3)
# print(arr)
# print(x)

# arr2 = np.array([1,2,3,4,5,6])
# y = np.where(arr%2==0)
# print(arr2)
# print(y)





