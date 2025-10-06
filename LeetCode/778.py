import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = []
        heapq.heappush(queue, (grid[0][0], 0, 0))
        visited = set((0,0))
        while queue:
            time, x, y = heapq.heappop(queue)
            if x == n - 1 and y == n - 1:
                return time
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n  or (nx, ny) in visited:
                    continue

                next_t = max(time, grid[nx][ny])
                visited.add((nx, ny))
                heapq.heappush(queue, (next_t, nx, ny))

        return -1
