

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = [0] * 26
        for i in s:
            cnt[ord(i) - ord('a')] += 1

        for i in range(t):
            next_cnt = [0] * 26
            next_cnt[0] = cnt[25]
            next_cnt[1] = (cnt[0] + cnt[25]) % MOD
            for j in range(2, 26):
                next_cnt[j] = cnt[j -1]
            cnt = next_cnt
        res = 0
        for i in range(26):
            res = (res + cnt[i]) % MOD
        return res