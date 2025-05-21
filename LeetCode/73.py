from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][j] = -10000019
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -10000019:
                    matrix[i][j] = 0
                    for k in range(i + 1, n):
                        if matrix[k][j] == -10000019:
                            break
                        matrix[k][j] = 0
                    for k in range(i -1, -1, -1):
                        if matrix[k][j] == -10000019:
                            break
                        matrix[k][j] = 0
                    for k in range(j + 1, m):
                        if matrix[i][k] == -10000019:
                            break
                        matrix[i][k] = 0
                    for k in range(j - 1, -1, -1):
                        if matrix[i][k] == -10000019:
                            break
                        matrix[i][k] = 0