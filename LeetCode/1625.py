

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        increment = {str(n): str((n + a) % 10) for n in range(10)}
        n = len(s)

        def add(cur_s):
            res = ""
            for i in range(n):
                res += cur_s[i] if i % 2 == 0 else increment[cur_s[i]]
            return res

        def rot(cur_s):
            return cur_s[n - b:] + cur_s[:n - b]

        seen = set()
        def dfs(cur_s):
            if cur_s in seen:
                return
            seen.add(cur_s)
            dfs(rot(cur_s))
            dfs(add(cur_s))
            return

        dfs(s)
        return min(seen)

