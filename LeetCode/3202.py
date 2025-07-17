from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 2
        cnt = [0] * n
        for i in range(n):
            cnt[i] = nums[i] % k
        for i in range(k):
            dp = [0] * k
            for j in range(n):
                mod = cnt[j]
                pos = (i - mod + k) % k
                dp[mod] = dp[pos] + 1
                res = max(res, dp[mod])
        return res