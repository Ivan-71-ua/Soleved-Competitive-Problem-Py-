from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        res = float('inf')
        n, m, t = len(nums), len(edges), 0
        dp = [0] * n
        time = [[0] * 2 for _ in range(n)]
        dgs = [[] for _ in range(n)]
        for a, b in edges:
            dgs[a].append(b)
            dgs[b].append(a)

        def dfs(cur, parent):
            dp[cur] ^= nums[cur]
            nonlocal t
            time[cur][0] = t
            t += 1
            for d in dgs[cur]:
                if parent == d:
                    continue
                dfs(d, cur)
                dp[cur] ^= dp[d]
            time[cur][1] = t
            t += 1

        dfs(0, -1)
        total = dp[0]

        def ancestor(prev, cur):
            return time[prev][0] <= time[cur][0] and time[cur][1] <= time[prev][1]

        def calc(a, b, c):
            return max(a, b, c) - min(a, b, c)

        for i in range(1, n):
            for j in range(i + 1, n):
                a, b, c = 0, 0, 0
                if ancestor(i, j):
                    a = dp[j]
                    b = dp[i] ^ dp[j]
                    c = total ^ dp[i]
                elif ancestor(j, i):
                    a = dp[i]
                    b = dp[i] ^ dp[j]
                    c = total ^ dp[j]
                else:
                    a = dp[i]
                    b = dp[j]
                    c = total ^ dp[i] ^ dp[j]

                res = min(res, calc(a, b, c))
        return res

