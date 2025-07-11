from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        diff = []
        if startTime[0] > 0:
            diff.append(startTime[0])
        for i in range(1, n):
            diff.append(startTime[i] - endTime[i -1])
        diff.append(eventTime - endTime[-1])
        res, l = 0, 0
        sum = 0
        for r in range(len(diff)):
            sum += diff[r]
            if r - l == k:
                res = max(res, sum)
                sum -= diff[l]
                l += 1
        res = max(res, sum)
        return res