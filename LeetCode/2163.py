import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 3
        pref, suff = [0] * n, [0] * n
        q = []
        cur_s = 0
        for i in range(n):
            cur_s += nums[i]
            heapq.heappush(q, -nums[i])
            while len(q) > k:
                cur_s -= abs(heapq.heappop(q))
            pref[i] = cur_s
        cur_s = 0
        q = []
        for i in range(n -1, -1, -1):
            cur_s += nums[i]
            heapq.heappush(q, nums[i])
            while len(q) > k:
                cur_s -= heapq.heappop(q)
            suff[i] = cur_s
        res = float('inf')
        for i in range(k -1, n - k, 1):
            res = min(res, pref[i] - suff[i + 1])
        return res