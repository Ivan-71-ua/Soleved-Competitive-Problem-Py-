from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = [0] * 501
        for n in arr:
            cnt[n] += 1
        res = -1
        for i in range(501):
            if cnt[i] and cnt[i] == i:
                res = i
        return res