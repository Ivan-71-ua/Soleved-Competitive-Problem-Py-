from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        cnt = [0] * 202
        min_neg = -300
        sum_pos = 0
        for n in nums:
            if not cnt[n + 100]:
                if n > 0:
                    sum_pos += n
                else:
                    min_neg = max(min_neg, n)
                cnt[100 + n] += 1
        if sum_pos:
            return sum_pos
        return min_neg
