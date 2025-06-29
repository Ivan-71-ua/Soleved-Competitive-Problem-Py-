from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        def fastPow(base, exp, mod):
            ans = 1
            while exp:
                if exp & 1:
                    ans = (ans * base) % mod
                base  = (base * base) % mod
                exp >>= 1
            return ans
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res = (fastPow(2, r - l, 10**9 + 7) + res) % (10**9 + 7)
                l += 1
        return res