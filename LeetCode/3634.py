from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_pos, n = 0, len(nums)
        window = 1
        for max_pos in range(n):
            while nums[max_pos] > nums[min_pos] * k:
                min_pos += 1
            window = max(window, max_pos - min_pos + 1)
        return n - window
