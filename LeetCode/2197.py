from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def lcm(a, b):
            return a * b // gcd(a, b)
        #But there are built-in functions [gcd, lcm] that work faster
        stack = []
        for num in nums:
            cur = num
            if not stack or gcd(cur, stack[-1]) > 1:
                cur = lcm(cur, stack.pop())
            stack.append(cur)
        return stack
