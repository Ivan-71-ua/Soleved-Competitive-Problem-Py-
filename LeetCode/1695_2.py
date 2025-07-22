


from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        cur_sum = 0
        cnt = set()
        l = 0
        for r in range(len(nums)):
            if nums[r] in cnt:
                while nums[l] != nums[r]:
                    cnt.remove(nums[l])
                    cur_sum -= nums[l]
                    l += 1
                l += 1
            else:
                cur_sum += nums[r]
                cnt.add(nums[r])
                res = max(res, cur_sum)
        return res