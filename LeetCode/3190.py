from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            cnt += min(3 - num % 3, num % 3)
        return cnt