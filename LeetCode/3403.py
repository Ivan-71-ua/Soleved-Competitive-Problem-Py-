
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        def lastSub(s):
            n, i, j = len(s), 0, 1
            while(j < n):
                k  = 0
                while(j + k < n and s[i + k] == s[j + k]):
                    k += 1
                if(j + k < n and s[i + k] < s[j + k]):
                    tmp = i
                    i = j
                    j = max(j + 1, tmp + k + 1)
                else:
                    j += k + 1
            return s[i:]
        if numFriends == 1:
            return word
        last = lastSub(word)
        n, m = len(word), len(last)
        return last[:min(m, n - numFriends + 1)]