from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        cnt = [0] * (n + 1)
        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            cnt[left] += stations[i]
            cnt[right] -= stations[i]

        def can(val):
            diff = cnt.copy()
            remain = k

            total = 0
            for i in range(n):
                total += diff[i]
                if total < val:
                    add = val - total
                    if add > remain:
                        return False
                    remain -= add
                    end = min(n, i + 2 * r + 1)
                    diff[end] -= add
                    total += add
            return True

        res = 0
        left, right = min(stations), sum(stations) + k
        while left <= right:
            mid = left + (right - left) // 2
            if can(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res