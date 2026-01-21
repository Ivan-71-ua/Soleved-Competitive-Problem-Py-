from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            for k in range(1, nums[i]):
                if k | (k + 1) == nums[i]:
                    ans[i] = k
                    break
        return ans