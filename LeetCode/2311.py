
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res, n, num = 0, len(s), 0
        for i in range(n -1, -1, -1):
            if s[i] == '0':
                res += 1
            else:
                if n - i - 1 > 32:
                    continue
                tmp = 2 ** (n - i - 1)
                if tmp + num <= k:
                    res += 1
                    num += tmp
        return res