# [1, 1, 2]
# solution: 2, [_, _, 2]

# [2, 3, 3, 4, 3, 4]
# solution: 4, [2, _, _, _, _, _]


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        duplicates = 1
        for i in range(1, len(nums)-1):
            if nums.count(nums[i]) > 1:
                duplicates += 1
        return duplicates


solution = Solution()
print(solution.removeDuplicates(nums=[2, 3, 3, 4, 3, 4]))
