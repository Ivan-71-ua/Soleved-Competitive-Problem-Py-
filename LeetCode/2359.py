from collections import deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [float('inf')] * n
        dist2 = [float('inf')] * n
        adj = [[] for _ in range(n)]
        for i in range(n):
            if edges[i] != -1:
                adj[i].append(edges[i])
        q = deque([node1])
        dist1[node1] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist1[v] > dist1[u] + 1:
                    dist1[v] = dist1[u] + 1
                    q.append(v)
        q = deque([node2])
        dist2[node2] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist2[v] > dist2[u] + 1:
                    dist2[v] = dist2[u] + 1
                    q.append(v)
        ans, dist = -1, float('inf')
        for i in range(n):
            if dist1[i] != float('inf') and dist2[i] != float('inf'):
                max_dist = max(dist1[i], dist2[i])
                if max_dist < dist:
                    dist = max_dist
                    ans = i
                elif max_dist == dist:
                    ans = min(ans, i)
        return ans