from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0]  * (2 * n)
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res