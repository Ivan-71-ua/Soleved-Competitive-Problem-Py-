
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(word)
        total = 1
        group = []
        cnt = 1
        for i in range(1, n):
            if word[i] == word[i -1]:
                cnt += 1
            else:
                group.append(cnt)
                cnt = 1
        group.append(cnt)
        for i in group:
            total = (total * i) % MOD
        if k <= len(group):
            return total

        dp = [0] * k
        dp[0] = 1
        for i in group:
            new_dp =[0] * k
            sum = 0
            for j in range(k):
                if j > 0:
                    sum = (sum + dp[j -1]) % MOD
                if j - i > 0:
                    sum = (sum - dp[j - i - 1] + MOD) % MOD
                new_dp[j] = sum
            dp = new_dp
        invalid = 0
        for i in range(len(group), k):
            invalid = (invalid + dp[i]) % MOD
        return (total - invalid + MOD) % MOD




