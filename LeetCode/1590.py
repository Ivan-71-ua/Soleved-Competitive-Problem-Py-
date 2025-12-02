from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        sums = sum(nums)
        if sums % p == 0:
            return 0

        target, curSum, res = sums % p, 0, n
        indexs = dict()
        indexs[0] = -1
        for i in range(n):
            curSum = (curSum + nums[i]) % p
            need_remove = (curSum - target + p) % p
            if need_remove in indexs:
                res = min(res, i - indexs[need_remove])

            indexs[curSum] = i
        return -1 if res == n else res