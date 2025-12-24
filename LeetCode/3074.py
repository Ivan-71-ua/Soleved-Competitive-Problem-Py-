from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
       need = sum(apple)
       capacity.sort(reverse=True)
       for i in range(len(capacity)):
           need -= capacity[i]
           if need < 1:
               return i + 1
       return -1