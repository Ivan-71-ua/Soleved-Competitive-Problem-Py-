from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2, k1, k2, n, m = 0, 0, 0, 0, len(nums1), len(nums2)
        for i in range(n):
            if nums1[i] == 0:
                k1 += 1
                sum1 += 1
            else:
                sum1 += nums1[i]
        for i in range(m):
            if nums2[i] == 0:
                k2 += 1
                sum2 += 1
            else:
                sum2 += nums2[i]
        if sum1 > sum2:
            sum1, sum2 = sum2, sum1
            k1, k2 = k2, k1
        if sum1 == sum2 or k1 * k2 > 0 or (k1 != 0 and k2 == 0):
            return sum2
        return -1