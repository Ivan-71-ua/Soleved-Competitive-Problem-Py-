


from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int):
        @lru_cache(None)
        def dfs(m: int, f: int, s: int):
            if f > s:
                f, s = s, f
            if f + s > m + 1:
                return dfs(m, m + 1 - s, m + 1 - f)
            if f + s == m + 1:
                return 1, 1
            nxt = (m + 1) // 2
            mn, mx = 1 << 30, -1
            if s <= nxt:
                for i in range(f):
                    nf = i + 1
                    for j in range(s - f):
                        e, l = dfs(nxt, nf, i + j + 2)
                        mn = min(mn, e)
                        mx = max(mx, l)
            else:
                sp = m + 1 - s
                gap = (m - 2 * sp + 1) // 2
                for i in range(f):
                    nf = i + 1
                    for j in range(sp - f):
                        e, l = dfs(nxt, nf, i + j + gap + 2)
                        mn = min(mn, e)
                        mx = max(mx, l)
            return mn + 1, mx + 1
        return list(dfs(n, firstPlayer, secondPlayer))
