


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        prev = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == '0':
                prev[i + 1] = i
            else:
                prev[i + 1] = prev[i]

        res = 0
        for i in range(1, n + 1):
            cnt0 = (1 if s[i - 1] == '0' else 0)
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - prev[j]) - cnt0

                if cnt0 * cnt0 <= cnt1:
                    res += min(j - prev[j], cnt1 - cnt0 * cnt0 + 1)
                j = prev[j]
                cnt0 += 1

        return res