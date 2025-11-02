from typing import List


class Solution:
    def countUnguarded(self, n: int, m: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * m for _ in range(n)]
        for i, j in guards:
            grid[i][j] = 1
        for i, j in walls:
            grid[i][j] = 1
        for i, j in guards:
            for k in range(i - 1, -1, -1):
                if grid[k][j] == 1:
                    break
                grid[k][j] = 2
            for k in range(i + 1, n):
                if grid[k][j] == 1:
                    break
                grid[k][j] = 2

            for k in range(j - 1, -1, -1):
                if grid[i][k] == 1:
                    break
                grid[i][k] = 2

            for k in range(j + 1, m):
                if grid[i][k] == 1:
                    break
                grid[i][k] = 2
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    cnt += 1
        return cnt

