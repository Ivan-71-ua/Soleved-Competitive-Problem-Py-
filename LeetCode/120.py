from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        path = [[0] * len(triangle[i]) for i in range(n)]
        path[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    path[i][j] = triangle[i][j] + path[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    path[i][j] = triangle[i][j] + path[i - 1][j - 1]
                else:
                    path[i][j] = min(path[i - 1][j], path[i - 1][j - 1]) + triangle[i][j]
        return min(path[n - 1][:])