from typing import List


class Solution:
    def rotate(self, vec):
        n = len(vec)
        m = len(vec[0])
        ret = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                ret[m - j - 1][i] = vec[i][j]
        return ret
    def minSum2(self, vec, u, d, l ,r):
        n = len(vec)
        m = len(vec[0])
        l_i, l_j = n * m, n * m
        r_i, r_j = 0, 0
        for i in range(u, d + 1):
            for j in range(l, r + 1 ):
                if vec[i][j]:
                    l_i = min(l_i, i)
                    l_j = min(l_j, j)
                    r_i = max(r_i, i)
                    r_j = max(r_j, j)
        if l_i > r_i:
            return 1e18
        return (r_i - l_i + 1) * (r_j - l_j + 1)

    def solve(self, vec):
        n, m = len(vec), len(vec[0])
        res = n * m
        for i in range(n - 1):
            for j in range(m - 1):
                res = min(res, self.minSum2(vec, 0, i, 0, m -1) +
                          self.minSum2(vec, i + 1, n -1, 0, j) +
                          self.minSum2(vec, i + 1, n -1, j + 1, m - 1))
                res = min(res, self.minSum2(vec, 0, i, 0, j) +
                          self.minSum2(vec, 0, i, j + 1, m -1) +
                          self.minSum2(vec, i + 1, n - 1, 0, m - 1))
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                res = min(res, self.minSum2(vec, 0, i, 0, m - 1) +
                          self.minSum2(vec, i + 1, j, 0, m - 1) +
                          self.minSum2(vec, j + 1, n - 1, 0, m - 1))
        return res


    def minimumSum(self, grid: List[List[int]]) -> int:
        rot = self.rotate(grid)
        return min(self.solve(grid), self.solve(rot))
