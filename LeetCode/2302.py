from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n, sum, res, l = len(nums), 0, 0, 0
        for i in range(n):
            sum += nums[i]
            while sum * (i - l + 1) > k:
                sum -= nums[l]
                l += 1
            res += i - l + 1
        return res
