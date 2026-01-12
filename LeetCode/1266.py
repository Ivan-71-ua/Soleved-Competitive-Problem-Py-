from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        dist, n = 0, len(points)

        for i in range(1, n):
            x, y = abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1])
            dist += max(x, y)
        return dist