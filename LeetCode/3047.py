from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n, res = len(bottomLeft), 0
        for i in range(n):
            x1, y1 = bottomLeft[i][0], bottomLeft[i][1]
            x2, y2 = topRight[i][0], topRight[i][1]
            for j in range(i + 1, n):
                x11, y11 = bottomLeft[j][0], bottomLeft[j][1]
                x12, y12 = topRight[j][0], topRight[j][1]
                x1_t = max(x1, x11)
                y1_t = max(y1, y11)
                x2_t = min(x2, x12)
                y2_t = min(y2, y12)
                if x1_t <= x2_t and y1_t <= y2_t:
                    res = max(res, min(x2_t - x1_t, y2_t - y1_t))
        return res * res