import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
transposed_matrix = matrix.T
print(matrix)
print(transposed_matrix)
print('--------------------')

print('reshape')
array = np.arange(1,13)
reshaped_array = array.reshape(3,4)
print(array)
print(reshaped_array)
print('--------------------')

print('reverse array')
reversed_array = array[::-1]
print(array)
print(reversed_array )
print('--------------------')

print('convert multidimensional array into unidirectional array')
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
flattened_array = matrix.flatten()
print(matrix)
print(flattened_array)