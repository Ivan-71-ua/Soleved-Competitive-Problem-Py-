from functools import cache
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        n, m = len(grid), len(grid[0])
        res = 0


        @cache
        def dfs(x, y, dicection, turn, target):
            nx, ny = x + DIRS[dicection][0], y + DIRS[dicection][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or target != grid[nx][ny]:
                return 0
            #turn_int = 1 if turn else 0
            max_step = dfs(nx, ny, dicection, turn, 2 - target)
            if turn:
                max_step = max(max_step, dfs(nx, ny, (dicection + 1) % 4, False, 2 - target))
            return max_step + 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for k in range(4):
                        res = max(res, dfs(i, j, k, True, 2) + 1)
        return res
