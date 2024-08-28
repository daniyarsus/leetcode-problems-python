# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        array = []
        if numRows % 2 == 0:
            for i in range(1, numRows):
                middle = i // 2
                print(middle, i)
                array.append([k for k in range(1, i + 1) if i == middle])
        return array


solution = Solution()
print(solution.generate(24))
