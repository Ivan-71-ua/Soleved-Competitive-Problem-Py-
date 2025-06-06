from inspect import stack


class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = [0] * 26
        st = []
        minChar = 0
        res = ""
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for c in s:
            st.append(ord(c) - ord('a'))
            cnt[ord(c) - ord('a')] -= 1
            while minChar != 26 and cnt[minChar] == 0:
                minChar += 1
            while st and st[-1] <= minChar:
                res += chr(st.pop() + ord('a'))
        return res
