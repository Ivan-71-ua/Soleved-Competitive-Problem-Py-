
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        n = len(num)
        for i in range(n - 2):
            cur = num[i:i + 3]
            if cur[0] == cur[1] == cur[2] and cur > res:
                res = cur
        return res