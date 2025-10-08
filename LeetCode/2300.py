import bisect
from typing import List



class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m, idx_greater = len(spells), len(potions), 0
        potions.sort()
        res = [0] * n
        for i in range(n):
            min_pover = ((success + spells[i] - 1) // spells[i])
            res[i] = max(0, m - bisect.bisect_left(potions, min_pover))
        return res