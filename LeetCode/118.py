from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[] for _ in range(numRows)]
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(i):
                if j != 0 or j != i - 1:
                    row[j] = ans[i -1][j - 1] + ans[i][j]
            ans[i] = row
        return ans