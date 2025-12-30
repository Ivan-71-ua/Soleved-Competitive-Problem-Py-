from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m, cnt = len(grid), len(grid[0]), 0
        for i in range(n - 3, -1, -1):
            for j in range(m - 3, -1, -1):
                print(i, j)
                can = True
                all_sum = set()
                nums = set()
                for x in range(3):
                    for y in range(3):
                        nums.add(grid[i + x][j + y])
                for k in range(1, 10):
                    if k not in nums:
                        can = False
                        break
                for k in range(10, 16):
                    if k in nums:
                        can = False
                        break
                all_sum.add(grid[i][j] + grid[i][j + 1] + grid[i][j + 2])
                all_sum.add(grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2])
                all_sum.add(grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2])

                all_sum.add(grid[i][j] + grid[i + 1][j] + grid[i + 2][j])
                all_sum.add(grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1])
                all_sum.add(grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2])

                all_sum.add(grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2])
                all_sum.add(grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j])

                if len(all_sum) != 1:
                    can = False

                cnt += can

        return cnt