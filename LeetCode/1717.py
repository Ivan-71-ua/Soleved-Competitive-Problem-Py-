
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        res = 0
        for i in range(len(s)):
            if x > y:
               if stack and stack[-1] == 'a' and s[i] == 'b':
                   res += x
                   stack.pop()
               else:
                   stack.append(s[i])
            else:
                if stack and stack[-1] == 'b' and s[i] == 'a':
                    res += y
                    stack.pop()
                else:
                    stack.append(s[i])
        stack2 = []
        for i in range(len(stack)):
            if x > y:
                if stack2 and stack2[-1] == 'b' and stack[i] == 'a':
                    res += y
                    stack2.pop()
                else:
                    stack2.append(stack[i])
            else:
                if stack2 and stack2[-1] == 'a' and stack[i] == 'b':
                    res += x
                    stack2.pop()
                else:
                    stack2.append(stack[i])
        return res

s = Solution()
s.maximumGain("aabbaaxybbaabb", 5,4)

