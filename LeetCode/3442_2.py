


class Solution:
    def maxDifference(self, s: str) -> int:
        max_od = 0
        min_ev = -1000
        cnt = [0] * 26
        for i in s:
            cnt[ord(i) - ord('a')] += 1
        for i in range(26):
            if cnt[i] == 0:
                continue
            if i & 1:
                max_od = max(max_od, cnt[i])
            else:
                min_ev = min(min_ev, cnt[i])
        return max_od - min_ev