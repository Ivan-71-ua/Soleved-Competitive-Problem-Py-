from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        if sum(nums) & 1:
            return 0
        return len(nums) - 1