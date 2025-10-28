from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i]
        cnt = 0
        for i in range(n):
            if nums[i] == 0:
                print(pref[i], (pref[-1] - pref[i]))
                if abs(pref[i] - (pref[-1] - pref[i])) == 0:
                    cnt += 2
                elif abs(pref[i] - (pref[-1] - pref[i])) == 1:
                    cnt += 1
        return cnt