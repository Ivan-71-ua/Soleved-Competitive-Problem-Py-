

class Solution:
    def smallestNumber(self, n: int) -> int:
        k = 1
        while n >= k:
            k <<= 1
        return k - 1