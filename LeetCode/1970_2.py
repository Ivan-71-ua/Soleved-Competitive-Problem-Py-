from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(row * col + col + 2)
        grid = [[0] * col for _ in range(row)]
        way = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))

        for i in range(row * col):
            x, y = cells[i]
            idx = x * col + y + 1
            grid[x - 1][y - 1] = 1
            for dx, dy in way:
                newx, newy = x + dx, y + dy
                if 0 <= newx - 1 < row and 0 <= newy - 1 < col and grid[newx - 1][newy - 1] == 1:
                    dsu.unite(idx, newx * col + newy + 1)

            if y == 1:
                dsu.unite(idx, 0)

            if y == col:
                dsu.unite(idx, -1)

            if dsu.union(0, -1):
                return i

        return -1



class DSU:
    def __init__(self, size):
        self.size = size
        self.parent = [0] * size
        self.rank = [1] * size
        for i in range(size):
            self.parent[i] = i

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return self.parent[x]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                px, py = py, px

            self.parent[py] = px
            self.rank[px] += self.rank[py]

    def union(self, x, y):
        return self.find(x) == self.find(y)