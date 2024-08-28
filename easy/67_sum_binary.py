# Input: a = "11", b = "1"
# Output: "100"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_decimal = int(a, 2) + int(b, 2)
        return bin(sum_decimal)[2:]


solution = Solution()
print(solution.addBinary("11", "1"))
