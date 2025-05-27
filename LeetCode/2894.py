
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1, sum2 = 0, 0
        for i in range(1, n + 1):
            if i % m == 0:
                sum2 += i
            else:
                sum1 += i
        return sum1 - sum2