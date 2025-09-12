

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        mydict = {}
        for ch in s:
            if ch in ['a', 'e', 'i', 'o', 'u']:
                mydict[ch] = 1
        if len(mydict) > 0:
            return True
        return False