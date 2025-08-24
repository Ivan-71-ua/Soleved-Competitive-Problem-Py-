from itertools import count
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        prev, cur = 0, 0
        for num in nums:
            if num:
                cur += 1
                res = max(res, cur)
                res = max(res, cur + prev)
            else:
                prev = cur
                cur = 0
        if res == len(nums):
            res -= 1
        return res