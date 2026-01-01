from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ost = 1
        for i in range(len(digits) - 1, -1, -1):
            new_val = ost + digits[i]
            digits[i] = new_val % 10
            ost = new_val // 10
        if ost:
            digits.insert(0, ost)
        return digits