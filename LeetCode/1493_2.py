from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, zero, start = 0, 0, 0
        for i in range(len(nums)):
            zero += (nums[i] == 0)
            while zero > 1:
                zero -= (nums[start] == 0)
                start += 1
            res = max(res, i - start)

        return res