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
        for i in range(n + 1, n * 7 + 100):
            if(good(i)):
                return i
        return -1
