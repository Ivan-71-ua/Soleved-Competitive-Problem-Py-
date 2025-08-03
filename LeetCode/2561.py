from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        res, min_e, n = 0, float('inf'), len(basket1)
        cnt = defaultdict(int)
        for i in range(n):
            cnt[basket1[i]] += 1
            cnt[basket2[i]] -= 1
            min_e = min(min_e, basket1[i], basket2[i])
        swap_need = []

        for v, f in cnt.items():
            if f % 2 != 0:
                return -1
            diff = abs(f // 2)
            for i in range(diff):
                swap_need.append(v)
        swap_need.sort()

        for i in range(len(swap_need) // 2):
            res += min(2 * min_e, swap_need[i])

        return res
