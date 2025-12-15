
class Solution:
    def countTriples(self, n: int) -> int:
        squares = set([i * i for i in range(1, n + 1)])
        result = 0
        for i in range(1, n + 1):
            cur_sqr = i * i
            for j in range(i + 1, n + 1):
                if cur_sqr + j * j in squares:
                    result += 2
        return result