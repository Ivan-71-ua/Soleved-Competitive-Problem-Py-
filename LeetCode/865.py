from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_d = -1

        def dfs(node, cur_d):
            nonlocal ans, max_d
            max_d = max(max_d, cur_d)
            if not node:
                return cur_d

            lf = dfs(node.left, cur_d + 1)
            rh = dfs(node.right, cur_d + 1)
            if lf == rh and lf == max_d:
                ans = node

            return max(lf, rh)

        dfs(root, 0)
        return ans