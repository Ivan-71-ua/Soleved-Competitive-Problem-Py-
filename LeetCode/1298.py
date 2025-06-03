from collections import deque
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        res = 0
        visited = [False] * n
        has_box = [False] * n
        can_open = [False] * n
        q = deque()
        for i in range(n):
            if status[i]:
                can_open[i] = True
        for i in initialBoxes:
            has_box[i] = True
            if can_open[i]:
                q.append(i)
                visited[i] = True
                res += candies[i]
        while q:
            cur = q.popleft()
            for g in keys[cur]:
                can_open[g] = True
                if has_box[g] and not visited[g]:
                    q.append(g)
                    visited[g] = True
                    res += candies[g]
            for g in containedBoxes[cur]:
                has_box[g] = True
                if can_open[g] and not visited[g]:
                    q.append(g)
                    visited[g] = True
                    res += candies[g]
        return res