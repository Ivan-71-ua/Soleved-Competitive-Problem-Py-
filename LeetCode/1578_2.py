from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res, prev = 0, 0
        for i in range(1, len(neededTime)):
            if colors[prev] == colors[i]:
                if neededTime[i] < neededTime[prev]:
                    res += neededTime[i]
                else:
                    res += neededTime[prev]
                    prev = i
            else:
                prev = i
        return res