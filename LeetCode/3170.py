
class Solution:
    def clearStars(self, s: str) -> str:
        stack = [ []  for _ in range(26) ]
        arr = list(s)
        res= ""
        for i in range(len(arr)):
            if arr[i] == '*':
                for j in range(26):
                    if stack[j]:
                        arr[stack[j].pop()] = '*'
                        break
            else:
                stack[ord(arr[i]) - ord('a')].append(i)

        for i in range(len(arr)):
            if arr[i] != '*':
                res += arr[i]
        return res