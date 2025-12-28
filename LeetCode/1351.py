from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        n, m = len(grid), len(grid[0])
        i, j = n - 1, 0
        while i > -1 and j < m:
            if grid[i][j] > -1:
                j += 1
            else:
                cnt += m - j
                i -= 1
        return cnt
