
class Solution:
    def longestBalanced(self, s: str) -> int:
        res, n = 0, len(s)

        for i in range(n):
            alph = [0] * 26
            for j in range(i, n):
                ch, tmp = ord(s[j]) - ord('a'), -1
                alph[ch] += 1

                for k in range(26):
                    if alph[k] != 0:
                        if tmp == -1:
                            tmp = alph[k]
                        elif tmp != alph[k]:
                            tmp = -1
                            break

                if tmp != -1:
                    res = max(res, j - i + 1)

        return res