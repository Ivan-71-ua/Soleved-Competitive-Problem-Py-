from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        n, m = len(strs), len(strs[0])
        is_sorted = [False] * (n - 1)

        for col in range(m):
            bad = False
            for i in range(n - 1):
                if not is_sorted[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                cnt += 1
                continue

            for i in range(n - 1):
                if not is_sorted[i] and strs[i][col] < strs[i + 1][col]:
                    is_sorted[i] = True

            if all(is_sorted):
                break

        return cnt