from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        increas, decreas = [1] * n, [1] * n
        for i in range(1, n):
            if nums[i] > nums[i -1]:
                increas[i] = increas[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                decreas[i] = decreas[i + 1] + 1
        for i in range(n - 1):
            res = max(res, min(increas[i], decreas[i + 1]))
        return res
