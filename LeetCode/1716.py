


class Solution:
    def totalMoney(self, n: int) -> int:
        sum = 0
        for i in range(n // 7):
            sum += (2 * (i + 1) + 6) * 7 // 2
        if n % 7:
            sum += (2 * ((n + 6) // 7) +( (n % 7) - 1)) * (n % 7) // 2

        return sum