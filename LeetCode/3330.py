
class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        prev = word[0]
        cnt = 1
        for i in range(1, len(word)):
            if word[i] == prev:
                cnt += 1
            else:
                res += cnt - 1
                prev = word[i]
                cnt = 1
        res += cnt - 1
        return res