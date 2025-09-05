
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 40):
            x = num1 - k * num2
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
        return -1