

class Solution:
    def kthCharacter(self, k: int) -> str:
        def cnt_ones(k):
            res = 0
            while k:
                res += 1
                k &= k - 1
            return res
        return chr(ord('a') + cnt_ones(k - 1))