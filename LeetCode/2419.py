from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = 0
        for num in nums:
            max_val = max(max_val, num)
        cur_l = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] == max_val:
                if(nums[i - 1] == nums[i]):
                    cur_l += 1
                else:
                    cur_l = 1

                res = max(res, cur_l)

        return res


