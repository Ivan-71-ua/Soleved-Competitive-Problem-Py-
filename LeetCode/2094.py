from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = []
        mp = [0] * 10
        for i in digits:
            mp[i] += 1
        for i in range(100, 1000, 2):
            fist, second, third = i // 100, (i // 10) % 10, i % 10
            fb, sb, tb = True, True, True
            if mp[fist]:
                mp[fist] -= 1
            else:
                fb = False
            if mp[second]:
                mp[second] -= 1
            else:
                sb = False
            if mp[third]:
                mp[third] -= 1
            else:
                tb = False
            if fb and sb and tb:
                cnt.append(i)
            if sb:
                mp[second] += 1
            if fb:
                mp[fist] += 1
            if tb:
                mp[third] += 1
        return cnt