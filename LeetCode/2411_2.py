
from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            j = i - 1
            while j > -1 and nums[j] | nums[i] != nums[j]:
                ans[j] = i - j + 1
                nums[j] |= nums[i]
                j -= 1
        return ans
