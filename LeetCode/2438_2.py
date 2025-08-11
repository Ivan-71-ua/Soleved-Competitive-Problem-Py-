from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        s_n = len(queries)
        ans = [0] * s_n
        powers = []
        i  = 0
        while i < 32:
            if (1 << i) & n:
                powers.append(1 << i)
            i += 1
        m = len(powers)
        pref = [0] * m
        pref[0] = powers[0]
        for i in range(1, m):
            pref[i] = (pref[i - 1] * powers[i]) % MOD

        for i in range(s_n):
            l, r = queries[i]
            if l > 0:
                inv = pow(pref[l -1], MOD - 2, MOD)
                ans[i] = (inv * pref[r]) % MOD
            else:
                ans[i] = pref[r]
        return ans
