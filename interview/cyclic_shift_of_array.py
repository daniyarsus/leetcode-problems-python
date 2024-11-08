arr = ['a', 'b', 'c', 'd', 'e']

k = 2


def shift_arr(arr: list[str], k: int) -> list[str]:
    temp = []
    for i in range(len(arr)):
        arr[i] = arr[i + k]

    return temp


print(shift_arr(arr, k))