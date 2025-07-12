import bisect
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        diff = []
        res, prev, cur, n = 0, 0, 0, len(startTime)
        if startTime[0] > 0:
            diff.append(startTime[0])
            cur = startTime[0]
        for i in range(1, n):
            diff.append(startTime[i] - endTime[i -1])
        if eventTime - endTime[-1] > 0:
            diff.append(eventTime - endTime[-1])
        diff.sort()
        for i in range(1, n + 1):
            prev = cur
            if i < n:
                cur = startTime[i] - endTime[i-1]
            else:
                cur = eventTime - endTime[i-1]
            free = endTime[i -1] - startTime[i-1]
            cnt = bisect.bisect_left(diff, free)
            cnt = len(diff) - cnt
            if prev >= free:
                cnt -=1
            if cur >= free:
                cnt -= 1
            if cnt > 0:
                res = max(res, prev + cur + free)
            else:
                res = max(res, prev + cur)
        return res

if __name__ == '__main__':
    s = Solution()
    s.maxFreeTime(21, [18,20],    [20,21])