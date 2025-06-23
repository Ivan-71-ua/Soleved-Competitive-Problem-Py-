



class Solution:
    def create_palindrome(self, num: int, odd: bool) -> int:
        result = num
        if odd:
            num //= 10
        while num > 0:
            result = result * 10 + num % 10
            num //= 10
        return result

    def is_palindrome_in_base(self, num: int, base: int) -> bool:
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base

        size = len(digits)
        for i in range(size // 2):
            if digits[i] != digits[size - 1 - i]:
                return False
        return True

    def kMirror(self, k: int, n: int) -> int:
        total = 0
        length = 1

        while n > 0:

            for i in range(length, length * 10):
                p = self.create_palindrome(i, odd=True)
                if self.is_palindrome_in_base(p, k):
                    total += p
                    n -= 1
                    if n == 0:
                        return total


            for i in range(length, length * 10):
                p = self.create_palindrome(i, odd=False)
                if self.is_palindrome_in_base(p, k):
                    total += p
                    n -= 1
                    if n == 0:
                        return total

            length *= 10

        return total
