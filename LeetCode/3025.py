from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        result, n = 0, len(points)
        for i in range(n):
            for j in range(i + 1, n):

                a1, b1 = points[i]
                a2, b2 = points[j]
                if a1 <= a2 and b1 >= b2:
                    rule = True
                    for k in range(n):
                        if not rule:
                            break
                        if k != i and k != j:
                            ap, bp = points[k]
                            if a1 <= ap and b1 >= bp and a2 >= ap and b2 <= bp:
                                rule = False
                    result += rule
        return result

