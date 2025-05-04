from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dom = [[0] * 10 for _ in range(10)]
        for a,b in dominoes:
            if a > b:
                a, b = b, a
            dom[a][b] += 1
        ans = 0
        for i in range(1, 10):
            for j in range(1, 10):
                ans += (dom[i][j] * (dom[i][j] - 1)) // 2
        return ans