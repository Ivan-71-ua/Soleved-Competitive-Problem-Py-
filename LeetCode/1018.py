from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n, cur = len(nums), 0
        ans = [False] * n
        for i in range(n):
            if nums[i]:
                cur *= 2
                cur += 1
            else:
                cur *= 2
            if cur % 5 == 0:
                ans[i] = True
        return ans