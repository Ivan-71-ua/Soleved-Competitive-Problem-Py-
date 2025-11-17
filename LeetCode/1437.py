from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        prev = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                print(prev, i)
                if prev > -1 and i - prev <= k:
                    return False
                prev = i
        return True