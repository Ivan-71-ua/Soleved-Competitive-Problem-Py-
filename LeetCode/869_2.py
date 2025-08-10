
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_dig(num):
            return sorted(str(num))

        target = count_dig(n)
        for i in range(31):
            if target == count_dig(1 << i):
                return True
        return False