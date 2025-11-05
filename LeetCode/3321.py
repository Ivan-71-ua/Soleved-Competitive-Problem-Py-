from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Helper:
    def __init__(self, x):
        self.x = x
        self.result = 0
        self.cnt = defaultdict(int)
        self.large = SortedList()
        self.small = SortedList()

    def get(self):
        return self.result

    def insert(self, num):
        if self.cnt[num] > 0:
            self.interval_remove((self.cnt[num], num))
        self.cnt[num] += 1
        self.interval_insert((self.cnt[num], num))

    def remove(self, num):
        self.interval_remove((self.cnt[num], num))
        self.cnt[num] -= 1
        if self.cnt[num] > 0:
            self.interval_insert((self.cnt[num], num))

    def interval_insert(self, p):
        if len(self.large) < self.x or p > self.large[0]:
            self.result += p[0] * p[1]
            self.large.add(p)
            if len(self.large) > self.x:
                will_remove = self.large[0]
                self.result -= will_remove[0] * will_remove[1]
                self.large.remove(will_remove)
                self.small.add(will_remove)
        else:
            self.small.add(p)

    def interval_remove(self, p):
        if p >= self.large[0]:
            self.result -= p[0] * p[1]
            self.large.remove(p)
            if self.small:
                will_add = self.small[-1]
                self.result += will_add[0] * will_add[1]
                self.small.remove(will_add)
                self.large.add(will_add)
        else:
            self.small.remove(p)


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        helper = Helper(x)
        res = []

        for i in range(len(nums)):
            helper.insert(nums[i])
            if i >= k:
                helper.remove(nums[i - k])
            if i >= k - 1:
                res.append(helper.get())

        return res

