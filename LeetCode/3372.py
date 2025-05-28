from collections import deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(node, edg, k):
            max = 1
            queue = deque([(node, -1, 0)])
            while queue:
                cur, par, deep = queue.popleft()
                if deep >= k:
                    break
                for nei in edg[cur]:
                    if nei != par:
                        max += 1
                        queue.append((nei, cur, deep + 1))
            return max
        n, m = len(edges1) + 1, len(edges2) + 1
        edg1 = [[] for _ in range(n)]
        edg2 = [[] for _ in range(m)]
        for u, v in edges1:
            edg1[u].append(v)
            edg1[v].append(u)
        for u, v in edges2:
            edg2[u].append(v)
            edg2[v].append(u)
        best = 0
        for i in range(m):
            cur = dfs(i, edg2, k - 1)
            if cur > best:
                best = cur
        res = [0] * n
        for i in range(n):
            res[i] = dfs(i, edg1, k) + (best if k > 0 else 0)
        return res
