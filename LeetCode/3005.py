from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = [0] * 101
        max_cnt = 0
        for num in nums:
            cnt[num] += 1
            max_cnt = max(max_cnt, cnt[num])
        sum = 0
        for k in cnt:
            if k == max_cnt:
                sum += k
        return sum