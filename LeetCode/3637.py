from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                can = True

                for f in range(1, i + 1):
                    if nums[f - 1] >= nums[f]:
                        can = False
                        break

                if not can:
                    continue

                for f in range(i + 1, j + 1):
                    if nums[f - 1] <= nums[f]:
                        can = False
                        break

                if not can:
                    continue

                for f in range(j + 1, n):
                    if nums[f - 1] >= nums[f]:
                        can = False
                        break


                if can:
                    return True
        return False
