import numpy as np

prices = np.array([100,200,300])
discount = np.array([0.5, 0.7, 0.9])
discount_prices = prices * discount
print(discount_prices)
print('--------------------------------')

prices = np.random.randint(100,500, size=(3,3))
discount = np.array([10,20,30])
discount_prices = prices + discount
print(prices)
print(discount_prices)
print('--------------------------------')


array = np.array([1,2,3,4,5])
print(np.all(array > 9))
print('--------------------------------')

print(np.any(array > 0))
print('--------------------------------')

array_a = np.array([1,2,3])
array_b = np.array([4,5,6])
concatenated_a = np.concatenate((array_a, array_a))
concatenated_ab = np.concatenate((array_a, array_b))
print(concatenated_a)
print(concatenated_ab)
print('--------------------------------')

stacked_v = np.vstack((array_a, array_b))
print(stacked_v)
print('--------------------------------')

satecked_h = np.hstack((array_a, array_b))
print(satecked_h)
print('--------------------------------')

array_c = np.arange(1,10)
split_array = np.split(array_c,3)
print(array_c)
print(split_array)