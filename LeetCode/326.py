


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        cur = 1
        while cur <= n:
            if cur == n:
                return True
            cur *= 3
        return False