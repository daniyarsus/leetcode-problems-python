# 1
# 1 * 2 = 2
# 1 * 2 * 3 = 6
# 1 * 2 * 3 * 4 = 24
# 1 * 2 * 3 * 4 * 5 = 120


def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print(power(3, 2))
