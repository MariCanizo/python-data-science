import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

#Suma
sum = A + B
print(A)
print(B)
print(sum)
print('------------------------')

print('multiplication')
product = np.dot(A, B)
print(product)
print('------------------------')

print('determinant and inverse')
A = np.array([[1,2],[3,4]])
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
print(A)
print(det_A)
print(inv_A)
print('------------------------')

print('solve Ax = b')
#Resolver Ax = b
b = np.array([9,11])
x = np.linalg.solve(A,b)
print(x)