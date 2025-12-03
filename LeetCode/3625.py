from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        slope_intercept = defaultdict(list)
        mid_slope = defaultdict(list)
        ans = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2

                if x2 == x1:
                    k = float('inf')
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx

                mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_intercept[k].append(b)
                mid_slope[mid].append(k)

        for trp in slope_intercept.values():

            if len(trp) == 1:
                continue

            cnt = defaultdict(int)
            for b_val in trp:
                cnt[b_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans += total_sum * count
                total_sum += count

        for par in mid_slope.values():

            if len(mid_slope) == 1:
                continue

            cnt = defaultdict(int)
            for k_val in par:
                cnt[k_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans -= total_sum * count
                total_sum += count

        return ans
