from collections import Counter
from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        cur_sum = 0
        cnt = Counter()
        l = 0
        for r in range(len(nums)):
            cnt[nums[r]] += 1
            cur_sum += nums[r]
            while cnt[nums[r]] > 1:
                cnt[nums[l]] -= 1
                cur_sum -= nums[l]
                l += 1
            res = max(res, cur_sum)
        return res