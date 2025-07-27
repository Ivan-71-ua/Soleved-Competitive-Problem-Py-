from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        unic = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != unic[-1]:
                unic.append(nums[i])
        cnt = 0
        for i in range(1, len(unic) - 1):
            if unic[i] > unic[i + 1] and unic[i] > unic[i - 1]:
                cnt += 1
            if unic[i] < unic[i + 1] and unic[i] < unic[i - 1]:
                cnt += 1
        return cnt
