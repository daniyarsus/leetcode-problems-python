# 1
# 1 * 2 = 2
# 1 * 2 * 3 = 6
# 1 * 2 * 3 * 4 = 24
# 1 * 2 * 3 * 4 * 5 = 120


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
