from typing import List


class Solution:
    digit = ""

    def plusOne(self, digits: List[int]) -> List[int]:
        try:
            for i in range(len(digits)):
                self.digit += str(digits[i])
        finally:
            int_digit = list(map(int, list(str(int(self.digit) + 1))))

        return int_digit
