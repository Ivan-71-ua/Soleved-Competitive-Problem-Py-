from collections import defaultdict


class Solution:

    def nextBeautifulNumber(self, n: int) -> int:
        def good(n):
            cnt = defaultdict(int)
            while n:
                cnt[n % 10] += 1
                n //= 10
            for k, v in cnt.items():
                if k != v:
                    return False
            return True
        while True:
            n += 1
            if good(n):
                return n
        return -1
