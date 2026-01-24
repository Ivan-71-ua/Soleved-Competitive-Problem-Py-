from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n, i, res = len(nums), 0, float("-inf")
        while i < n // 2:
            res = max(res, nums[i] + nums[n - i -1])
            i += 1
        return res