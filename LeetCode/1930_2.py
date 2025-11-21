
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3:
            return 0

        cnt = 0
        used = set()
        for i in range(len(s)):
            if s[i] not in used:
                used.add(s[i])
                r = s.rfind(s[i])
                cnt += len(set(s[i + 1:r]))
        return cnt