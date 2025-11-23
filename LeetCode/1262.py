from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
       sums = sum(nums)

       if sums % 3 == 0:
           return sums

       one1, one2 = 10000, 10000
       two1, two2 = 10000, 10000

       for num in nums:
           if num % 3 == 1:
               if one1 > num:
                   one2 = one1
                   one1 = num
               elif one2 > num:
                   one2 = num
           elif num % 3 == 2:
               if two1 > num:
                   two2 = two1
                   two1 = num
               elif two2 > num:
                   two2 = num
       print(one1, one2, two1, two2 )
       if sums % 3 == 1:
           return sums - min(one1, two1 + two2)
       return sums - min(two1, one1 + one2)


