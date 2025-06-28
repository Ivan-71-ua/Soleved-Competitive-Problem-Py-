from collections import defaultdict
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_n = sorted(nums)
        needed = defaultdict(int)
        for i in range(len(nums) - k, len(nums)):
            needed[sorted_n[i]] += 1
        res = []
        for i in nums:
            if needed[i] > 0:
                res.append(i)
                needed[i] -= 1
            if len(res) == k:
                break
        return res