from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        sums = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                sums[i] = sums[i - 1] + 1
        cnt = 0
        for i in range(n - 2, -1, -1):
            if ratings[i - 1] > ratings[i]:
                sums[i -1] = max(sums[i] + 1, sum[i -1])
            cnt += sums[i -1]
        return cnt + sums[-1]