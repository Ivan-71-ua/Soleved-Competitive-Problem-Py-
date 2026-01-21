from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            if nums[i] & 1:
                ans[i] = nums[i] & ~(((nums[i] + 1) & ~nums[i]) >> 1)
        return ans