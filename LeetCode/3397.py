from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt, prev = 0, -float('inf')
        for i in range(len(nums)):
            cur_l = min(max(nums[i] - k, prev + 1), nums[i] + k)
            if cur_l > prev:
                prev = cur_l
                cnt += 1
        return cnt