

class Solution:
    def numSub(self, s: str) -> int:
        mod = 10 ** 9 + 7
        cnt, result = 0, 0
        for ch in s:
            if ch == '0':
                result = (result + (cnt * (cnt + 1) // 2)) % mod
                cnt = 0
            else:
                cnt += 1
        result = (result + (cnt * (cnt + 1) // 2)) % mod
        return result
