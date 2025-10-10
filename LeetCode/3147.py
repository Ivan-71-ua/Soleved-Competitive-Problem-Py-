from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n, res = len(energy), float('-inf')
        dp = [0]  * n
        for i in range(n - 1, -1, -1):
            dp[i] = energy[i]
            if i + k < n:
                dp[i] = dp[i + k] + energy[i]
            res = max(res, dp[i])
        print(dp)
        return res