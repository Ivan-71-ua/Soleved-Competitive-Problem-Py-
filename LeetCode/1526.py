from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res, cur_v = 0, 0
        for k in target:
            if k > cur_v:
                res += k - cur_v
            cur_v = k
        return res