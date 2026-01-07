from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs_sum(root):
            if not root:
                return 0
            return root.val + dfs_sum(root.left) + dfs_sum(root.right)
        res, total_sum = float('-inf'), dfs_sum(root)
        def dfs(root):
            if not root:
                return 0
            subtree_sum = dfs(root.left) + dfs(root.right) + root.val
            nonlocal res, total_sum
            res = max(res, (total_sum - subtree_sum) * subtree_sum)

            return subtree_sum

        dfs(root)
        return res % (1000000000 + 7)