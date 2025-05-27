
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum2, mult = 0, 0
        while mult + m <= n:
            mult += m
            sum2 += mult
        sum1 = n * (n + 1) // 2 - sum2
        return sum1 - sum2