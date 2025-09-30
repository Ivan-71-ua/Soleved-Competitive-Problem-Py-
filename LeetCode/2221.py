from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while(len(nums) > 1):
            tmp = [0] * (len(nums) - 1)
            for i in range(len(tmp)):
                tmp[i] = (nums[i] + nums[i + 1]) % 10
            nums = tmp
        return nums[0]