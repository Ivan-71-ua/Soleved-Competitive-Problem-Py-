from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append(nums[i:i + 3])
        return res
