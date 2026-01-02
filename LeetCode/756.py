from collections import defaultdict
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allow_dict = defaultdict(set)

        for a, b, c in allowed:
            allow_dict[(a, b)].add(c)
        print(allow_dict)
        def get_layer(node):
            res = ['']
            for i in range(1, len(node)):
                a, b = node[i - 1], node[i]
                if (a, b) in allow_dict:
                    res = [c + k for k in allow_dict[(a, b)] for c in res]
                else:
                    return []
            return res

        visited = set()

        def dfs(node):
            if len(node) == 1:
                return True

            if node in visited:
                return False

            for nxt in get_layer(node):
                if dfs(nxt):
                    return True

            visited.add(node)
            return False

        return dfs(bottom)
