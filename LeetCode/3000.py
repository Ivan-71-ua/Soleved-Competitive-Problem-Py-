from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = -1
        d = -1
        for a, b in dimensions:
            if a * a + b * b > d:
                res = a * b
                d = a * a + b * b
            elif a * a + b * b == d:
                res = max(res, a * b)
        return res