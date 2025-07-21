
class Solution:
    def makeFancyString(self, s: str) -> str:
        tmp = []
        n = len(s)
        if n < 3:
            return s
        for c in range(n - 2):
            if s[c] != s[c + 1] or s[c + 1] != s[c + 2]:
                tmp.append(s[c])
        tmp.append(s[n - 2])
        tmp.append(s[n - 1])
        return "".join(tmp)

