from typing import List


from collections import deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, ans, seen = len(colors), 0, 0
        graph = [[0] * 26 for _ in range(n)]
        indegree = [0] * n
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            seen += 1
            color = ord(colors[u]) - ord('a')
            graph[u][color] += 1
            ans = max(ans, graph[u][color])

            for v in adj[u]:
                for k in range(26):
                    graph[v][k] = max(graph[v][k], graph[u][k])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if seen == n:
            return ans
        return -1

