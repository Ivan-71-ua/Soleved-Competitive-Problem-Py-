from bisect import bisect
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if (idx := bisect.bisect(letters, target)) < len(letters):
            return letters[idx]
        return letters[0]