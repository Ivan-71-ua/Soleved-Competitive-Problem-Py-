from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        roads = [[float('inf')] * 26 for _ in range(26)]

        for a, b, c in zip(original, changed, cost):
            f, s = ord(a) - ord('a'), ord(b) - ord('a')
            roads[f][s] = min(c, roads[f][s])

        for k in range(26):
            for i in range(26):
                if roads[i][k] == float('inf'):
                    continue
                for j in range(26):
                    if roads[k][j] == float('inf'):
                        continue
                    roads[i][j] = min(roads[i][j], roads[i][k] + roads[k][j])

        min_cost = 0
        for a, b in zip(source, target):
            if a != b:
                f, s = ord(a) - ord('a'), ord(b) - ord('a')
                if roads[f][s] == float('inf'):
                    return -1
                min_cost += roads[f][s]

        return min_cost
