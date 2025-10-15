from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res, cnt, prevcnt = 0, 1, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i -1]:
                cnt += 1
            else:
                prevcnt, cnt = cnt, 1
            res = max(res, min(cnt, prevcnt))
            res = max(res, cnt // 2)
        return res

