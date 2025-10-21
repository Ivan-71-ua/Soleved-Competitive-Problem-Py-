from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxValue = max(nums) + k + 2
        cnt = [0] * maxValue
        for i in nums:
            cnt[i] += 1

        for i in range(1, maxValue):
            cnt[i] += cnt[i - 1]

        res = 0
        for i in range(maxValue):
            left = max(0, i -  k)
            right = min(i + k, maxValue - 1)
            total = cnt[right] - (cnt[left - 1] if left else 0)
            freq = cnt[i] - (cnt[i - 1] if i else 0)
            res = max(res, freq + min(numOperations, total - freq))

        return res