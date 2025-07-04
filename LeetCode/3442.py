
class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        odd = []
        even = []
        for i in range(26):
            if( cnt[i] == 0):
                continue
            if cnt[i] & 1:
                odd.append(cnt[i])
            else:
                even.append(cnt[i])
        res = -1000
        for i in range(len(odd)):
            for j in range(len(even)):
                res = max(res, odd[i] - even[j])
        return res