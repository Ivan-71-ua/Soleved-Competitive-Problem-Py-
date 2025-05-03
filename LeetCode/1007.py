from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        s1 = [0] * 7
        s2 = [0] * 7
        n = len(tops)
        for i in range(n):
            s1[tops[i]] += 1
            s2[bottoms[i]] += 1
        res = float('inf')
        for i in range(1, 7):
            if s1[i]:
                cnt, swap = 0, 0
                for j in range(n):
                    if tops[j] == i:
                        cnt += 1
                    elif bottoms[j] == i:
                        cnt += 1
                        swap += 1
                if cnt == n:
                    res = min(res, swap)
            if s2[i]:
                cnt, swap = 0, 0
                for j in range(n):
                    if bottoms[j] == i:
                        cnt += 1
                    elif tops[j] == i:
                        cnt += 1
                        swap += 1
                if cnt == n:
                    res = min(res, swap)

        return res if res != float('inf') else -1
