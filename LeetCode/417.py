from collections import deque
from typing import List



class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        way = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(ocean):
            q = deque([])
            used = [[False] * m for _ in range(n)]
            for i in range(n):
                if ocean:
                    q.append((i, 0))
                    used[i][0] = True
                    pacific.add((i, 0))
                else:
                    q.append((i, m - 1))
                    used[i][m - 1] = True
                    atlantic.add((i, m - 1))
            for i in range(m):
                if ocean:
                    q.append((0, i))
                    used[0][i] = True
                    pacific.add((0, i))
                else:
                    q.append((n - 1, i))
                    used[n - 1][i] = True
                    atlantic.add((n - 1, i))

            while q:
                cur_i, cur_j = q.popleft()
                for i, j in way:
                    next_i = cur_i + i
                    next_j = cur_j + j
                    if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m or used[next_i][next_j] or heights[cur_i][
                        cur_j] > heights[next_i][next_j]:
                        continue

                    if ocean:
                        pacific.add((next_i, next_j))
                    else:
                        atlantic.add((next_i, next_j))
                    used[next_i][next_j] = True
                    q.append((next_i, next_j))

        dfs(True)
        dfs(False)
        return list(pacific & atlantic)
























