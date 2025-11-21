from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        cnt = 0
        prev1, prev2 = -1, -1
        for l, r in range(intervals):
            if prev2 < l:
                cnt += 2
                prev1, prev2 = r - 1, r
            elif prev1 < l:
                if r == prev2:
                    prev2 = r
                else:
                    prev2 = r - 1
                if prev1 > prev2:
                    prev1, prev2 = prev2, prev1
                cnt += 1
        return cnt