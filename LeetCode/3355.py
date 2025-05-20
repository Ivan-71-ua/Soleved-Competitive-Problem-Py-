from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        pref = [0] * (n + 1)
        for l, r in queries:
            pref[l] -= 1
            pref[r + 1] += 1
        for i in range(1, n + 1):
            pref[i] += pref[i - 1]
        isZero = True
        for i in range(n):
            nums[i] = max(0, nums[i] + pref[i])
            if nums[i] != 0:
                isZero = False
                break
        return isZero