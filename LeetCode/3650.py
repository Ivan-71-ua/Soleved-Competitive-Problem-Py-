from heapq import heappop, heappush
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist = [float('inf')] * n
        visited = [False] * n
        eg = [[] for _ in range(n)]
        dist[0] = 0
        hp = [(0, 0)]
        for a, b, v in edges:
            eg[a].append((b, v))
            eg[b].append((a, v * 2))

        while hp:
            v, a = heappop(hp)

            if a == n - 1:
                return v

            if visited[a]:
                continue
            visited[a] = True

            for next_p, v_p in eg[a]:
                if v + v_p < dist[next_p]:
                    dist[next_p] = v + v_p
                    heappush(hp, (v + v_p, next_p))

        return -1







