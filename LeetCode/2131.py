from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        cnt = [26 * [0] for _ in range(26)]
        for word in words:
            i, j = ord(word[0]) - ord('a'), ord(word[1]) - ord('a')
            cnt[i][j] += 1
        odd = False
        for i in range(26):
            for j in range(i, 26):
                if i == j:
                    if cnt[i][j] & 1 and not odd:
                        res += 2
                        odd = True
                    res += (cnt[i][j] // 2) * 4
                else:
                    res += min(cnt[i][j], cnt[j][i]) * 4
        return res