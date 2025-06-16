from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [nums[0]] * n
        for i in range(1, n):
            pref[i] = min(pref[i - 1], nums[i])
        res = -1
        for i in range(1, n):
            if nums[i] > pref[i - 1]:
                res = max(res, nums[i] - pref[i - 1])
        return res
