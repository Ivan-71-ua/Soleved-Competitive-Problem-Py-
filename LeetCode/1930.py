class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cnt, n = 0, len(s)
        used = [False] * 26

        def lastIndexOf(ch):
            for i in range(n - 1, -1, -1):
                if s[i] == ch:
                    return i
            return -1

        for i in range(n):
            if used[ord(s[i]) - ord('a')]:
                continue
            used[ord(s[i]) - ord('a')] = True
            k = lastIndexOf(s[i])
            if k == i:
                continue
            set_ch = [False] * 26
            for i in range(i + 1, k):
                set_ch[ord(s[i]) - ord('a')] = True
            cnt += sum(set_ch)

        return cnt