# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return [0, True]

            lHeight, lBal = dfs(node.left)
            rHeight, rBal = dfs(node.right)
            

            if abs(lHeight - rHeight) > 1:
                return [1 + max(lHeight, rHeight), False]
            else:
                return [1 + max(lHeight, rHeight), lBal and rBal]

        return dfs(root)[1]
        