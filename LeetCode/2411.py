from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        last_bit = [-1] * 32
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            bit = 0
            while bit < 32:
                if nums[i] & (1 << bit):
                    last_bit[bit] = i
                bit += 1
            idx = i
            for j in range(32):
                idx = max(idx, last_bit[j])
            ans[i] = idx - i + 1
        return ans
