from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val, res, cur_l = 0, 0, 0
        for num in nums:
            if max_val < num:
                max_val = num
                cur_l = 0
                res = 0
            if max_val == num:
                cur_l += 1
            else:
                cur_l = 0
            res = max(res, cur_l)
        return res
