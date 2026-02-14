from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        seen = [0] * (max(nums) + 1)

        for i in range(n):
            if n - i <= ans: break
            tmp = [0, 0]

            for j in range(i, n):
                if seen[nums[j]] != i + 1:
                    seen[nums[j]] = i + 1
                    tmp[nums[j] & 1] += 1

                if tmp[0] == tmp[1]:
                    ans = max(ans, j - i + 1)



        return ans