import bisect
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res, n = 0, len(nums)
        for i in range(n - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, n - 1):
                k = bisect.bisect_left(nums, nums[i] + nums[j], k)
                res += k - j - 1
        return res
