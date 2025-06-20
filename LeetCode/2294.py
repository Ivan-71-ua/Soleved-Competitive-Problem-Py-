from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        mins, maxs = min(nums), max(nums)
        sets  = [0] * (maxs + 1)
        for i in nums:
            sets[i] = 1
        res = 0
        for i in range(mins, maxs + 1):
            if sets[i] and i - mins > k:
                res += 1
                mins = i
        return res + 1