from collections import defaultdict
from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.save1 = nums1
        self.save2 = nums2
        self.cnt = defaultdict(int)
        for n in nums2:
            self.cnt[n] += 1

    def add(self, index: int, val: int) -> None:
        self.cnt[self.save2[index]] -= 1
        self.save2[index] += val
        self.cnt[self.save2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for n in self.save1:
            diff = tot - n
            if diff in self.cnt:
                res += self.cnt[diff]
        return res