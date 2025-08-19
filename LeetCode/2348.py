
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, cnt = 0, 0
        for num in nums:
            if num:
                res += cnt * (cnt + 1) // 2
                cnt = 0
            else:
                cnt += 1
        res += cnt * (cnt + 1) // 2
        return res
