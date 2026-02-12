from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        res, n = 0, len(s)

        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1

                if len(set(cnt.values())) == 1:
                    res = max(res, j - i + 1)

        return res