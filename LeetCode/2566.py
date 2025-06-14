
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_digit = '9'
        for c in s:
            if c != '9':
                max_digit = c
                break
        min_digit = s[0]
        maxn = 0
        minn = 0
        for c in s:
            maxn = maxn * 10 + (9 if c == max_digit else int(c))
            minn = minn * 10 + (0 if c == min_digit else int(c))

        return maxn - minn
