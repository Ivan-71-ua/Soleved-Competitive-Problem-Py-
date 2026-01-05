from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cnt_neg, mins = 0, float('inf')
        sums = 0
        n, m = len(matrix), len(matrix[0])
        for i  in range(n):
            for j in range(m):
                sums += abs(matrix[i][j])
                mins = min(mins, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    cnt_neg += 1

        if cnt_neg & 1:
            sums -= 2 * mins

        return sums