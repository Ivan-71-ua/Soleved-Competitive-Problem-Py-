from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        nums.reverse()
        cnt = 0
        while len(nums) > 1:
            can = True
            min_v, min_i = float('inf'), -1
            for j in range(1, len(nums)):
                if nums[j - 1] < nums[j]:
                    can = False
                if min_v >= nums[j] + nums[j - 1]:
                    min_v = nums[j] + nums[j - 1]
                    min_i = j
            if can:
                return cnt
            cnt += 1
            nums[min_i - 1] = min_v
            nums.pop(min_i)

        return cnt

