
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = list(map(int, s))
        while len(nums) > 2:
            tmp = []
            for i in range(1, len(nums)):
                tmp.append((nums[i] + nums[i - 1]) % 10)
            nums = tmp
        return nums[0] == nums[1]