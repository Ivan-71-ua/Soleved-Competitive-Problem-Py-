
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(cur,  n):
            res = 0
            neig = cur + 1
            while cur <= n:
                res += min(n + 1, neig) - cur
                cur *= 10
                neig *= 10
            return res

        i , cur = 1, 1
        while i < k:
            step = count(cur, n)
            if i + step <= k:
                cur += 1
                i += step
            else:
                cur *= 10
                i += 1
        return cur