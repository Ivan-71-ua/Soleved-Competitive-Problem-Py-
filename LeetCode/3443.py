
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n, N, S, W, E, ans = len(s), 0, 0, 0, 0, 0
        for i in range(n):
            if s[i] == 'N':
                N += 1
            elif s[i] == 'S':
                S += 1
            elif s[i] == 'W':
                W += 1
            elif s[i] == 'E':
                E += 1
            dk = k
            dx = ans(N - S) + 2 * min(N, S, dk)
            dk = max(0, dk - min(N, S))
            dy = ans(E - W) + 2 * min(E, W, dk)
            ans = max(ans, dx + dy)
        return ans