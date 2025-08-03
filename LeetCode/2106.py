from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        sumv, l, res = 0, 0, 0
        for r in range(len(fruits)):
            sumv += fruits[r][1]
            while l <= r and (fruits[r][0] - fruits[l][0]) + min(abs(startPos - fruits[l][0]), abs(startPos - fruits[r][0])) > k:
                sumv -= fruits[l][1]
                l += 1
            res = max(res, sumv)
        return res