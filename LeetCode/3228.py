
class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        cnt = 0
        for i in range(0, len(s) - 1):
            if s[i] == '1':
                cnt += 1
            if s[i] == '1' and s[i + 1] == '0':
                result += cnt
        return result