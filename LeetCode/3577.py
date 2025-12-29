from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        root = complexity[0]
        less = 0
        for num in complexity:
            if num <= root:
                less += 1
        if less > 1:
            return 0
        else:
            res = 1
            for i in range(2, len(complexity)): res = (res * i) % MOD
            return res