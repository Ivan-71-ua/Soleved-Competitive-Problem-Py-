from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt_even, cnt_odd, dp_odd, dp_even = 0, 0, 0, 0
        for n in  nums:
            if n & 1:
                cnt_odd += 1
                dp_odd = max(dp_odd, dp_even + 1)
            else:
                cnt_even += 1
                dp_even = max(dp_even, dp_odd + 1)
        return max(cnt_even, cnt_odd, dp_even, dp_odd)