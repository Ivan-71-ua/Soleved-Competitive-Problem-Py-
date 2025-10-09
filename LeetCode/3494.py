from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m  = len(skill), len(mana)
        time = [0] * n
        for i in range(m):
            cur_time = 0
            for j in range(n):
                cur_time = max(cur_time, time[j]) + skill[j] * mana[i]
            time[n - 1] = cur_time
            for j in range(n - 2, -1, -1):
                time[j] = time[j + 1] - skill[j + 1] * mana[i]
        return time[n - 1]