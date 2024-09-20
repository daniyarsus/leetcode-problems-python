from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return sum_(nums, target)


def sum_(nums: List[int], target: int, n: int = 0, result: List[int] = None) -> List[int]:
    if n >= len(nums):
        return result

    result.append(nums[n])

    return sum_(nums, target, n + 1, result)


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
