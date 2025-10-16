from typing import List, Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = Counter(x % value for x in  nums)
        mx = 0
        while cnt[mx % value]:
            cnt[mx % value] -= 1
            mx += 1
        return mx