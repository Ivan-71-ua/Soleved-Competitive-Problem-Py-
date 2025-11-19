from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for n in nums:
            if n == original:
                original *= 2
        return original