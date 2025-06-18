from collections import defaultdict
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        res, n, total = 0, len(arr), 0
        cnt = defaultdict(int)
        for num in arr:
            cnt[num] += 1

        freq = sorted(cnt.values(), reverse=True)
        for c in freq:
            total += c
            res += 1
            if total >= n // 2:
                return res
        return res

