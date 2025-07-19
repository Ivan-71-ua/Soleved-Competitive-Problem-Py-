from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        for i in range(1, len(folder)):
            start = res[-1]
            start += "/"
            if not folder[i].startswith(start):
                res.append(folder[i])
        return res