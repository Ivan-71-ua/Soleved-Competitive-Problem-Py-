

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b, res = 0, 0, len(s)

        for ch in s:
            a += (ch == 'a')

        for ch in s:
            if ch == 'a':
                a -= 1
            res = min(res, a + b)
            if ch == 'b':
                b += 1
        return res