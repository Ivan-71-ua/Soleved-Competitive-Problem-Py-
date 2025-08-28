from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(1, n):
            x, y = 0, i
            tmp = []
            while x < n and y < n:
                tmp.append(grid[x][y])
                x, y = x + 1, y + 1
            tmp.sort()
            for j in range(len(tmp)):
                grid[j][i + j] = tmp[j]

        for i in range(n):
            x, y = i, 0
            tmp = []
            while x < n and y < n:
                tmp.append(grid[x][y])
                x, y = x + 1, y + 1
            tmp.sort(reverse=True)
            for j in range(len(tmp)):
                grid[i + j][j] = tmp[j]

        return grid