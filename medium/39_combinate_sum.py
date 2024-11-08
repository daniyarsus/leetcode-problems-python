from typing import List, Dict

class Solution:
    def combinationSum(
            self,
            candidates: List[int],
            target: int
    ) -> List[List[int]]:
        result = []
        self.main(candidates, target, [], result)
        return result

    def main(
            self,
            candidates: List[int],
            target: int,
            current: List[int],
            result: List[List[int]]
    ) -> List[List[int]]:
        if target == 0:
            result.append(list(current))
            return
        if target < 0:
            return

        for i in range(len(candidates)):
            current.append(candidates[i])
            self.main(candidates, target - candidates[i], current, result)
            current.pop()

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7, 1], 9))