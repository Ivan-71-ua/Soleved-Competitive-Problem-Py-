from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        cnty = defaultdict(int)
        totalSum, ans = 0, 0
        for _, b in points:
            cnty[b] += 1
        for v in cnty.values():
            edge = v * (v - 1) // 2
            ans = (ans + edge * totalSum) % MOD
            totalSum += edge
        return ans
