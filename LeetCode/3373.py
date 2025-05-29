from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(node, parent, egj, deep, color):
            res = 1 - deep % 2
            color[node] = deep % 2
            for nei in egj[node]:
                if nei != parent:
                    res += dfs(nei, node, egj, deep + 1, color)
            return res
        n, m = len(edges1) + 1, len(edges2) + 1
        egj1 = [[] for _ in range(n)]
        egj2 = [[] for _ in range(m)]
        color1 = [0] * n
        color2 = [0] * m
        for u, v in edges1:
            egj1[u].append(v)
            egj1[v].append(u)
        for u, v in edges2:
            egj2[u].append(v)
            egj2[v].append(u)
        odd1 = dfs(0, -1, egj1, 0, color1)
        even1 = n - odd1
        odd2 = dfs(0, -1, egj2, 0, color2)
        even2 = m - odd2
        res = [0] * n
        for i in range(n):
            if color1[i]:
                res[i] = even1 + max(odd2, even2)
            else:
                res[i] = odd1 + max(odd2, even2)
        return res
