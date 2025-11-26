from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n, m, mod = len(grid), len(grid[0]), 1000000007
        dp = [[[0] * k for _ in range(m)] for _ in range(n)]

        dp[0][0][grid[0][0] % k] = 1

        for i in range(n):
            for j in range(m):
                for r in range(k):
                    prev = (r - grid[i][j] + k) % k
                    if i > 0:
                        dp[i][j][r] += dp[i - 1][j][prev]
                    if j > 0:
                        dp[i][j][r] += dp[i][j - 1][prev]

                    dp[i][j][r] %= mod

        return dp[-1][-1][0]
