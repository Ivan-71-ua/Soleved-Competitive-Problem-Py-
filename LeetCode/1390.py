from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(n):
            if n < 2:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        sums = 0
        for num in nums:
            p = round(num ** (1/3))
            if p**3 == num and is_prime(p):
                sums += 1 + p + p*p + num
                continue

            i = 2
            while i * i <= num:
                if num % i == 0:
                    j = num // i
                    if i != j and is_prime(j) and is_prime(i):
                        sums += 1 + j + i + num
                    break
                i += 1


        return sums



