from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first = [-1, 0]
        second = [-1, 0]
        res = 0
        for i in range(len(fruits)):
            if first[0] == -1 or first[0] == fruits[i]:
                first[0] = fruits[i]
                first[1] += 1
            elif  second[0] == -1 or second[0] == fruits[i]:
                second[0] = fruits[i]
                second[1] += 1
                second, first = first, second
            else:
                cnt, idx = 0, i - 1
                while idx > -1 and fruits[idx] == first[0]:
                    idx -= 1
                    cnt += 1
                first[1] = cnt
                second[0] = fruits[i]
                second[1] = 1
                first, second = second, first
            res = max(res, first[1] + second[1])
        return res