from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n, res = len(nums), []
        cnt = [0] * n
        for i in nums:
            if cnt[i]:
                res.append(i)
            cnt[i] += 1
        return res