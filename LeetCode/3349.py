from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def increas(idx):
            for i in range(idx + 1, idx + k):
                if nums[i] < nums[i - 1]:
                    return False
            return True
        for i in range(len(nums) - k):
            if increas(i) and increas(i + k):
                return True
        return False