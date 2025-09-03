from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        cnt, n = 0, len(points)
        points.sort(key = lambda x: (x[0], -x[1]))

        for a in range(n - 1):
            minX, maxX = points[a][0] - 1, float('inf')
            minY, maxY = -float('inf'), points[a][1] + 1
            for b in range(a +1, n):
                if (points[b][0] < maxX and points[b][0] > minX and
                        points[b][1] < maxY and points[b][1] > minY):
                    cnt += 1
                    minX, minY = points[b][0], points[b][1]
        return cnt

