from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = [0] * (1 << 17)
        max_v = 0
        dp[0] = 1
        for num in nums:
            for i in range(max_v, -1, -1):
                dp[i | num] += dp[i]

            max_v |= num
        return dp[max_v]
