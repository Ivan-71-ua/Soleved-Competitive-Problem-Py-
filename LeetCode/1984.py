from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        res = float("inf")

        for i in range(len(nums) - k + 1):
            res = min(res, nums[i] - nums[i + k - 1])

        return res
