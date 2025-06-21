
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = [0] * 26
        for c in word:
            cnt[ord(c) - ord('a')] += 1
        ans = float('inf')
        for i in range(26):
            if cnt[i] == 0:
                continue
            cur_remove = 0
            for j in range(26):
                if cnt[j] == 0 or i == j:
                    continue
                if(cnt[j] < cnt[i]):
                    cur_remove += cnt[j]
                else:
                    cur_remove += max(0, cnt[j] - k - cnt[i])
            ans = min(ans, cur_remove)
        return ans

# Example usage:
sol = Solution()
print(sol.minimumDeletions("dabdcbdcdcd", 2))  # Example input