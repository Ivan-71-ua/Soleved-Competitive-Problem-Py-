from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(row * col + col + 2)
        grid = [[0] * col for _ in range(row)]
        way = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(len(cells) - 1, -1, -1):
            x, y = cells[i]
            idx = x * col + y + 1
            grid[x - 1][y - 1] = 1
            for dx, dy in way:
                newx, newy = x + dx, y + dy
                if 0 <= newx - 1 < row and 0 <= newy - 1 < col and grid[newx - 1][newy - 1] == 1:
                    dsu.unite(idx, newx * col + newy + 1)

            if x == 1:
                dsu.unite(idx, 0)

            if x == row:
                dsu.unite(idx, col * row + 2)

            if dsu.union(0, col * row + 2):
                return i

        return -1


class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [0] * n
        self.rank = [1] * n
        for i in range(n):
            self.parent[i] = i

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            if self.rank[pa] < self.rank[pb]:
                pa, pb = pb, pa
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]
        return self.parent[a]

    def union(self, a, b):
        return self.find(a) == self.find(b)
