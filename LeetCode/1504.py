from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res, n , m = 0, len(mat), len(mat[0])
        row = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j == 0:
                    row[i][j] = mat[i][j]
                else:
                    row[i][j] = 0 if mat[i][j] == 0 else row[i][j - 1] + 1

                cur = row[i][j]
                for k in range(i, -1, -1):
                    cur = min(cur, row[k][j])
                    if cur == 0:
                        break
                    res += cur
        return res