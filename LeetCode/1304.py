from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n & 1:
            res.append(0)
        for i in range(n // 2):
            res.append(-(i + 1))
            res.append(i + 1)
        return res
