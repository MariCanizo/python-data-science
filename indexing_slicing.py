import numpy as np 

array = np.array([10,20,30,40,50])
print(array[1])
print(array[-1])

print(array[1:4])

print(array[1:7])
print(array[-1:-7])

array = np.array([10,20,30,40,50])
bool_index = array > 25
print(bool_index)
print(type(bool_index))

index = [2,0,3]
print(array[index])

array = np.random.randint(1, 10, size=(3,3))
print(array)
print(array[0,1])

print(array[:2,:2])