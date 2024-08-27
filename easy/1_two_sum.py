# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] == target:
                return [i, i+1]


solution = Solution()
print(solution.twoSum(nums=[2,7,11,15], target=26))
