from collections import defaultdict
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            even = defaultdict(int)
            odd = defaultdict(int)
            for j in range(i, n):
                if nums[j] & 1:
                    odd[nums[j]] += 1
                else:
                    even[nums[j]] += 1
                if len(odd) == len(even):
                    ans = max(ans, j - i + 1)

        return ans