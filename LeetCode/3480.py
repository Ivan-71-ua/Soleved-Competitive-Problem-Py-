from typing import List


class Solution:
    def maxSubarrays(self, n: int, conf: List[List[int]]) -> int:
        top1, top2, res, max_bonus = 0, 0, 0, 0
        left = [[0] * 2 for _ in range(n + 1)]
        bonus = [0] * (n + 1)
        for a, b in conf:
            if a > b:
                a, b = b, a
            if left[b][0] < a:
                left[b][1] = left[b][0]
                left[b][0] = a
            elif left[b][1] < a:
                left[b][1] = a

        for i in range(1, n + 1):
            for a in left[i]:
                if top1 < a:
                    top2 = top1
                    top1 = a
                elif top2 < a:
                    top2 = a
            res += i - top1
            if top1:
                bonus[top1] += top1 - top2
                max_bonus = max(max_bonus, bonus[top1])
        return max_bonus + res