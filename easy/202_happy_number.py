# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(n + 1):
            if i**2 + (i+1)**2 == n:
                print(i**2, (i+1)**2)
                return True


solution = Solution()
print(solution.isHappy(5))
