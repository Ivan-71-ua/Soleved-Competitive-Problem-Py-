from heapq import heappop, heappush
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dp = [[float('inf')] * m for _ in range(n)]
        dp[0][0] = 0
        pq = [(0, 0, 0, 1)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            t, x, y, d = heappop(pq)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    nt = max(t, moveTime[nx][ny]) + d
                    if nt < dp[nx][ny]:
                        dp[nx][ny] = nt
                        if d == 1:
                            heappush(pq, (nt, nx, ny, 2))
                        else:
                            heappush(pq, (nt, nx, ny, 1))

        return dp[-1][-1]
