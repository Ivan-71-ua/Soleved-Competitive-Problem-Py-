from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] == key:
                l, r = max(0, i - k), min(n -1, i + k)
                for j in range(l, r + 1):
                    if nums[j] == key and j > i:
                        break
                    if nums[j] == -1:
                        continue
                    nums[j] = -1
                    ans.append(j)
        return ans
