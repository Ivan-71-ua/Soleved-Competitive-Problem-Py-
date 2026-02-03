from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n, i = len(nums), 0

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        p = i

        if i == 0 or i >= n - 2:
            return False

        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        q = i

        if q == p or q >= n - 1:
            return False

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1


