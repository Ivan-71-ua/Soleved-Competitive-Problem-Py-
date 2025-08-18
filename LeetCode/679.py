from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ls = [float(c) for c in cards]
        return self.solve(ls)

    def solve(self, ls_n):
        if len(ls_n) == 1:
            return abs(ls_n[0] - 24.0) < 1e-6
        n = len(ls_n)
        for i in range(n):
            for j in range(n):

                if i == j:
                    continue

                next = []
                for k in range(n):
                    if k != i and k != j:
                        next.append(ls_n[k])

                a, b = ls_n[i], ls_n[j]
                res = [a + b, a - b, b - a, a * b]
                if abs(a) > 1e-6:
                    res.append(b / a)
                if abs(b) > 1e-6:
                    res.append(a / b)

                for val in res:
                    if self.solve(next + [val]):
                        return True
        return False



