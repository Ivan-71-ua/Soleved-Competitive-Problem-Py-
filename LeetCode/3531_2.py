from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        cordX = [[float('inf'), float('-inf')] for _ in range(n + 1)]
        cordY = [[float('inf'), float('-inf')] for _ in range(n + 1)]

        for x, y in buildings:
            cordX[x] = [min(y, cordX[x][0]), max(y, cordX[x][1])]
            cordY[y] = [min(x, cordY[y][0]), max(x, cordY[y][1])]

        cnt = 0
        for x, y in buildings:
            if cordX[x][1] <= y or cordX[x][0] >= y or cordY[y][1] <= x or cordY[y][0] >= x:
                continue
            cnt += 1

        return cnt


