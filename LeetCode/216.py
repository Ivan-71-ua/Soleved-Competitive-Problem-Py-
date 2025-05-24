from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(k, n, start, cur, total):
            if len(cur) == k:
                if total == n:
                    res.append(cur[:])
                return
            for i in range(start, 10):
                if total + i > n:
                    break
                cur.append(i)
                dfs(k, n, i + 1, cur, total + i)
                cur.pop()
        dfs(k, n, 1, [], 0)
        return res