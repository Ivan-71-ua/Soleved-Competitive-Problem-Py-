
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        max_digit = '9'
        for c in s:
            if c != '9':
                max_digit = c
                break
        min_digit = '@'
        first = False
        if s[0] != '1':
            min_digit = s[0]
            first = True
        else:
            for c in s:
                if c != '1' and c != '0':
                    min_digit = c
                    break
        maxn, minn = 0, 0
        for c in s:
            maxn = maxn * 10 + (9 if c == max_digit else int(c))
            if first:
                minn = minn * 10 + (1 if c == min_digit else int(c))
            else:
                minn = minn * 10 + (0 if c == min_digit else int(c))
        return maxn - minn