from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def can_live(t):
            need, curSum = n * t, 0
            for battery in batteries:
                curSum += min(battery, t)
                if curSum >= need:
                    return True
            return curSum >= need

        l, r = 0, sum(batteries) // n
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if can_live(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res


