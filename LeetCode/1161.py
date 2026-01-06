from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res, max_sum = -1,  float('-inf')
        queue, level = deque([root]), 1
        while queue:
            size = len(queue)
            curr_sum = 0
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curr_sum += node.val

            if curr_sum > max_sum:
                max_sum = curr_sum
                res = level
            level += 1
        return res


