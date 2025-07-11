from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        events = sorted(events, key=lambda x: x[1])
        def binary_search(start):
            res = -1
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if events[mid][1] < start:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res

        for i in range(1, n + 1):
            prev = binary_search(events[i -1][0])
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i -1][j], dp[prev + 1][j - 1] + events[i - 1][2])
        return dp[n][k]

