from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        nums.reverse()
        n, cnt = len(nums), 0
        for i in range(n):
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
            nums = nums[:min_i - 1] + [min_v] +  nums[min_i + 1:]

        return -1

