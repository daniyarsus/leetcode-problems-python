arr = ['a', 'b', 'c', 'a', 'd']

res = []

for index, value in enumerate(arr):
    if value == 'a':
        res.append(index)


print(res)