from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        res, n = 0, len(fruits)

        res += sum(fruits[i][i] for i in range(n))

        def dp():
            cur = [float('-inf')] * n
            prev = [float('-inf')] * n
            prev[n - 1] = fruits[0][n - 1]
            for i in range(1, n - 1):
                for j in range(max(n - i - 1, i + 1), n):
                    best = prev[j]
                    if j > 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    cur[j] = fruits[i][j] + best
                prev, cur = cur, prev
            return prev[n - 1]

        res += dp()
        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
        res += dp()

        return res
