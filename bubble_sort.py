# [1, 4, 3, 6, 4, 7]
# [1, 4, 3, 6, 4, 7]
# [1, 3, 4, 6, 4, 7]
# [1, 3, 4, 4, 6, 7]


def bubble_sort(array: list[int]) -> list[int]:
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    print(array)

bubble_sort(array=[1, 4, 3, 6, 4, 7])
