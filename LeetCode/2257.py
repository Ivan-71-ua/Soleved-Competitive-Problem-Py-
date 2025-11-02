from typing import List


class Solution:
    def countUnguarded(self, n: int, m: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cant = set()
        for i, j in guards:
            cant.add((i, j))
        for i, j in walls:
            cant.add((i, j))
        used = set()
        for i, j in guards:
            for k in range(i - 1, -1, -1):
                if (k, j) in cant:
                    break
                used.add((k, j))

            for k in range(i + 1, n):
                if (k, j) in cant:
                    break
                used.add((k, j))

            for k in range(j - 1, -1, -1):
                if (i, k) in cant:
                    break
                used.add((i, k))

            for k in range(j + 1, m):
                if (i, k) in cant:
                    break
                used.add((i, k))
        print(cant)
        print(used)

        return n * m - len(cant) - len(used)


