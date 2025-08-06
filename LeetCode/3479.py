from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt, n = 0, len(fruits)
        m = int(n ** 0.5)
        sections = (n + m  - 1) // m
        sections_max = [0] * sections
        for i in range(n):
            sections_max[i // m] = max(sections_max[i // m], baskets[i])

        for i in range(n):
            find = 1
            for j in range(sections):
                if sections_max[j] < fruits[i]:
                    continue
                choose = False
                sections_max[j] = 0
                for k in range(m):
                    pos = j * m + k
                    if pos < n and baskets[pos] >= fruits[i] and not choose:
                        choose = True
                        baskets[pos] = 0
                    if pos < n:
                        sections_max[j] = max(baskets[pos], sections_max[j])
                find = 0
                break

            cnt += find
        return cnt

