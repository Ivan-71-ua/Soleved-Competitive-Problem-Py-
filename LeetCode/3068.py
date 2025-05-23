from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * n
        sum = 0
        for i in range(n):
            sum += nums[i]
            diff[i] = (nums[i] ^ k) - nums[i]
        diff.sort(reverse=True)
        for i in range(1, n, 2):
            if diff[i] + diff[i - 1] < 0:
                break
            sum += diff[i] + diff[i - 1]
        return sum
