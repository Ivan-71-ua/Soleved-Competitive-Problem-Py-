
from typing import List


class Solution:
    def exp4sum(self, num):
        cnt = 0
        base = 1
        i = 1
        while True:
            l = 1 << (i - 1) * 2
            r = (1 << (i * 2)) - 1
            if l > num:
                break
            count_on_base = min(r, num) - l + 1
            cnt += count_on_base * base

            base += 1
            i += 1
        return cnt
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for a, b in queries:
           cur_s = self.exp4sum(b) - self.exp4sum(a - 1)
           res += (cur_s + 1) // 2
        return res
