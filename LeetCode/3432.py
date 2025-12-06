from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        cnt = 0
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            left += nums[i]
            right = nums[i]
            if not ((left - right) & 1):
                cnt += 1

        return cnt