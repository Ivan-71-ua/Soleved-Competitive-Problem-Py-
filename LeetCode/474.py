from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}
        for s in strs:
            ones, zeros = 0, 0
            for ch in s:
                if ch == '1':
                    ones += 1
                else:
                    zeros += 1

            new_dp = {}
            for k, v in dp.items():
                prev_zeros, prev_ones = k
                new_zeros, new_ones = prev_zeros + zeros, prev_ones + ones
                if new_zeros <= m and new_ones <= n:
                    if (new_zeros, new_ones) not in dp:
                        new_dp[(new_zeros, new_ones)] = v + 1
                    elif dp[(new_zeros, new_ones)] < v + 1:
                        new_dp[(new_zeros, new_ones)] = v + 1
            dp.update(new_dp)
        return max(dp.values())

