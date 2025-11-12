from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        g, ones,  n = 0, 0, len(nums)
        for num in nums:
            ones += num == 1
            g = gcd(g, num)

        if ones:
            return len(nums) - ones

        if g > 1:
            return -1

        minLen = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    minLen = min(minLen, j - i + 1)
                    break
        return minLen + n - 2