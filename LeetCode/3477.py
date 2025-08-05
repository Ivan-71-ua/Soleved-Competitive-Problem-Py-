from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        cnt = 0
        for i in range(n):
            l = -1
            for j in range(n -1, -1, -1):
                if baskets[j] and fruits[i] <= baskets[j]:
                    l = j
            if l != -1:
                cnt += 1
                baskets[l] = 0
        return n - cnt