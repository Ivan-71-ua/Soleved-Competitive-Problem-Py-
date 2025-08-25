from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n ,m  = len(mat), len(mat[0])
        mn_max = max(n, m)
        tmp = [[] for _ in range(mn_max * 2)]
        for i in range(n):
            for j in range(m):
                tmp[i + j].append(mat[i][j])
        res = []
        k =0
        for st in tmp:
            if st:
                if k & 1:
                    res.extend(st[::])
                else:
                    res.extend(st[::-1])
                k +=1
        return res
