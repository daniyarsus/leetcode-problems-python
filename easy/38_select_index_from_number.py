# [1, 2, 4] 5
# solution: 3

# [1, 2, 4] 3
# solution: 2


class Solution:
    def selectIndex(self, array: list[int], target: int) -> int:
        if len(array) and array[-1] <= target:
            return len(array) + 1
        for i in range(len(array)):
            if array[i] > target and target < array[i+1]:
                return i

solution = Solution()
print(solution.selectIndex(array=[1, 3, 5, 7, 9], target=6))
