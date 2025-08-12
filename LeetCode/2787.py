
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        unic_el = []
        for i in range(1, n + 1):
            if (i ** x) > n:
                break
            unic_el.append(i ** x)
        print(unic_el)
        for el in unic_el:
            for i in range(n, el - 1, -1):
                dp[i] = (dp[i] + dp[i - el]) % 1000000007
        return dp[n]
