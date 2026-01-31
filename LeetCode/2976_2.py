from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        gr = [[] for _ in range(26)]

        for a, b, c in zip(original, changed, cost):
            ai, bi = ord(a) - ord('a'), ord(b) - ord('a')
            gr[ai].append((bi, c))

        def dijkstra(start):
            heap = [(0, start)]
            cost = [float('inf')] * 26
            cost[start] = 0

            while heap:
                w, p = heappop(heap)

                if cost[p] < w:
                    continue

                for np, nw in gr[p]:
                    if w + nw < cost[np]:
                        cost[np] = w + nw
                        heappush(heap, (w + nw, np))

            return cost

        roads = [dijkstra(i) for i in range(26)]
        min_cost = 0

        for a, b in zip(source, target):
            if a != b:
                ai, bi = ord(a) - ord('a'), ord(b) - ord('a')
                if roads[ai][bi] == float('inf'):
                    return -1
                min_cost += roads[ai][bi]

        return min_cost

