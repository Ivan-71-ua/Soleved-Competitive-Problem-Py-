
class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_v, max_c = 0, 0
        cnt = [0] * 26
        for ch in s:
            if ch in 'aeiou':
                cnt[ord(ch) - ord('a')] += 1
                max_v = max(max_v, cnt[ord(ch) - ord('a')])
            else:
                cnt[ord(ch) - ord('a')] += 1
                max_c = max(max_c, cnt[ord(ch) - ord('a')])
        return max_v + max_c