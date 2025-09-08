from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def non_zero(num):
            while num != 0:
                if num % 10 == 0:
                    return False
                num = num // 10
            return True
        for i in range(1, n):
            if non_zero(i) and non_zero(n - i):
                return [i, n - i]
        return []
