array = [num for num in range(10)]

for index, num in enumerate(array):
    print(index, num)


array_1 = [num for num in range(10)]
array_2 = [num for num in range(10)]

for arr1, arr2 in zip(array_1, array_2):
    print('array 1 value = ', arr1, 'array 2 value = ', arr2)
