
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [1] * (n + 1)
        res, share, MOD = 0, 0, 10**9 + 7
        for i in range(2, n + 1):
            if i - delay > 0:
                share = (share + dp[i - delay] + MOD) % MOD
            if i - forget > 0:
                share = (share - dp[i - forget] + MOD) % MOD
            dp[i] = share

        for i in range(n - forget + 1, n + 1):
            res = (res + dp[i]) % MOD

        return res



