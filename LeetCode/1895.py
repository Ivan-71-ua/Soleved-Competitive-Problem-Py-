from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        sum_col, sum_row = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]

        for i in range(n):
            sum_row[i][0] = grid[i][0]
            for j in range(1, m):
                sum_row[i][j] = sum_row[i][j - 1] + grid[i][j]

        for i in range(m):
            sum_col[0][i] = grid[0][i]
            for j in range(1, n):
                sum_col[j][i] = sum_col[j - 1][i] + grid[j][i]

        for edge in range(min(n, m), 1, -1):

            for i in range(n - edge + 1):
                for j in range(m - edge + 1):
                    sample_sum = sum_row[i][j + edge - 1] - (0 if j == 0 else sum_row[i][j - 1])

                    check = True

                    for x in range(i + 1, i + edge):
                        if sample_sum != sum_row[x][j + edge - 1] - (0 if j == 0 else sum_row[x][j - 1]):
                            check = False
                            break

                    if not check:
                        continue

                    for y in range(j, j + edge):
                        if sample_sum != sum_col[i + edge - 1][y] - (0 if i == 0 else sum_col[i - 1][y]):
                            check = False
                            break

                    if not check:
                        continue

                    d1, d2 = 0, 0
                    for k in range(edge):
                        d1 += grid[i + k][j + k]
                        d2 += grid[i + k][j + edge - k - 1]
                    if d1 == d2 and d1 == sample_sum:
                        return edge
        return 1

