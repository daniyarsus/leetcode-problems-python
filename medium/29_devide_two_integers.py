from typing import List


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        data = str(dividend / divisor).split('.')
        print(data)
        main(data)


def main(data: List[str], n: int = 0, result: int = 0) -> int:
    if n >= len(data[-1]):
        return result

    if int(data[-1][n]) >= 5 and int(data[-1][n]) <= 9:
        ...

    main(data, n + 1, result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.divide(10, 3))