from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        l_y, l_x, r_y, r_x = 1111, 1111, -1, -1
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    l_x = min(l_x, i)
                    r_x = max(r_x, i)
                    l_y = min(l_y, j)
                    r_y = max(r_y, j)
        return (r_x - l_x + 1) * (r_y - l_y + 1)