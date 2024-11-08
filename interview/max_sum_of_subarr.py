max_sum = 0

arr = [[1, 2], [1, 4, 4, 3], [1, 4, 1]]
for i in range(len(arr)):
    if max_sum < sum(arr[i]):
        max_sum = sum(arr[i])


print(max_sum)
