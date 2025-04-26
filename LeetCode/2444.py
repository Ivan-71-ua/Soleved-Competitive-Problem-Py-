from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n, ans, min_i, max_i, bad_i = len(nums), 0, -1, -1, -1
        for i in range(n):
            if nums[i] < minK  or nums[i] > maxK:
                bad_i = i
            if nums[i]  == minK:
                min_i = i
            if nums[i] == maxK:
                max_i = i
            ans += max(0, min(min_i, max_i) - bad_i)
        return ans
