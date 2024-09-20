class Solution:
    def countAndSay(self, n: int) -> str:
        return count(n)


def count(data: int, n: int = 1, result: str = "") -> str:
    if data == 1:
        result = 1
        return result

    if len(result) >= n:
        return result

    if n >= data + 1:
        return result

    if data > 1:
        result += (str(n)) * 2
        result += (str(n) + str(n + 1))

    return count(data, n + 1, result)


sol = Solution()
print(sol.countAndSay(5))
