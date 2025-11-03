import heapq
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n, res = len(neededTime), 0
        q = [neededTime[0]]
        for i in range(1, n):
            if colors[i - 1] != colors[i]:
                while len(q) > 1:
                    res += heapq.heappop(q)
                heapq.heappop(q)
            heapq.heappush(q, neededTime[i])

        while len(q) > 1:
            res += heapq.heappop(q)
        return res