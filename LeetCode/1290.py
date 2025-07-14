from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res, cnt = 0, 0
        def dfs(node):
            if node is None:
                return
            dfs(node.next)
            nonlocal res, cnt
            res += (1 << cnt) * node.val
            cnt += 1
        dfs(head)
        return res
