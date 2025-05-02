from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res = 0
        mp = defaultdict(int)
        for row in matrix:
            tpl = tuple(row)
            if tpl[0]:
                tpl = tuple([0 if n else 1 for n in tpl])
            mp[tpl] += 1
            res = max(res, mp[tpl])

        return res
