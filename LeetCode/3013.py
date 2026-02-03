from typing import List

from sortedcontainers import SortedList


class Container:
    def __init__(self, k: int):
        self.k = k
        self.smallest = SortedList()
        self.others = SortedList()
        self.cur_sum = 0

    def get_sum(self) -> int:
        return self.cur_sum

    def balance(self) -> None:
        while len(self.smallest) < self.k and len(self.others) > 0:
            x = self.others[0]
            self.smallest.add(x)
            self.others.remove(x)
            self.cur_sum += x

        while len(self.smallest) > self.k:
            x = self.smallest[-1]
            self.others.add(x)
            self.smallest.remove(x)
            self.cur_sum -= x

    def add(self, num: int) -> None:
        if len(self.others) > 0 and num >= self.others[0]:
            self.others.add(num)
        else:
            self.smallest.add(num)
            self.cur_sum += num
        self.balance()

    def erase(self, num: int) -> None:
        if num in self.smallest:
            self.smallest.remove(num)
            self.cur_sum -= num
        elif num in self.others:
            self.others.remove(num)
        self.balance()



class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        cnt = Container(k - 2)

        for i in range(1, k - 1):
            cnt.add(nums[i])

        ans = cnt.get_sum() + nums[k - 1]

        for i in range(k, n):
            j = i - dist - 1
            if j > 0:
                cnt.erase(nums[j])
            cnt.add(nums[i - 1])
            ans = min(ans, cnt.get_sum() + nums[i])

        return ans + nums[0]



