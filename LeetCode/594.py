from collections import defaultdict
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for i  in nums:
            cnt[i] += 1
        res = 0
        for key, val in cnt.items():
            if key + 1 in cnt:
                res = max(res, val + cnt[key + 1])
        return res