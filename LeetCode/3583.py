from collections import defaultdict
from typing import List, Counter


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        cnt = 0
        suff = Counter(nums)
        pref = defaultdict(int)
        for num in nums:
            target = num * 2
            if target in suff:
                zero = num == 0
                cnt = (cnt + (pref[target] * (suff[target] - zero)) % MOD) % MOD
            pref[num] += 1
            suff[num] -= 1
        return cnt

