from collections import deque


class Solution:

      def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
            def check(sub):
                  cnt, i =0, 0
                  size = len(sub)
                  for c in s:
                        if c == sub[i]:
                              i += 1
                              if i == size:
                                    cnt += 1
                                    i = 0
                                    if cnt >= k:
                                          return True
                  return False
            res = ""
            q = deque([""])
            while q:
                  cur = q.popleft()
                  for c in "abcdefghijklmnopqrstuvwxyz":
                        next = cur + c
                        if check(next):
                              res = next
                              q.append(next)
            return res

