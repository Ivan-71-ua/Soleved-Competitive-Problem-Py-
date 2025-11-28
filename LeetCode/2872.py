from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        cnt = 0
        graf = [[] for _ in range(n)]

        for a, b in edges:
            graf[a].append(b)
            graf[b].append(a)

        def dfs(node, parent):
            cur = values[node]

            for next in graf[node]:
                if next != parent:
                    cur += dfs(next, node)

            if cur % k == 0:
                nonlocal cnt
                cnt += 1
                cur = 0

            return cur


        dfs(0, -1)
        return cnt
