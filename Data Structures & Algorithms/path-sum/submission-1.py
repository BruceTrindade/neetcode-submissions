# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, current_sum, targetSum):
        if not root:
            return False

        current_sum += root.val

        if not root.left and not root.right:
            return current_sum == targetSum  
        return self.dfs(root.left, current_sum, targetSum) or self.dfs(root.right, current_sum, targetSum)     

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
       return self.dfs(root, 0, targetSum)

        