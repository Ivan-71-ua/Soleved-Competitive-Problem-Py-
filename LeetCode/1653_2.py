



class Solution:
    def minimumDeletions(self, s: str) -> int:
        b, res = 0, 0

        for ch in s:
            if ch == 'b':
                b += 1
            elif b:
                res += 1
                b -= 1


        return res