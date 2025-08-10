
from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n & (n - 1) == 0: return True
        dig = []
        while n:
            dig.append(str(n % 10))
            n //= 10

        perm = permutations(dig)
        for cur in perm:
            if cur[0] != '0':
                num = int(''.join(cur))
                if num & (num - 1) == 0: return True
        return False





