# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#

class Solution:
    def dfs(self, root) -> int:
        if not root:
            return 0    

        height_right = self.dfs(root.right)
        height_left = self.dfs(root.left)   

        if height_right == -1 or height_left == -1:
            return -1

        if abs(height_right - height_left) > 1: 
            return -1 
        else: 
            return 1 + max(height_right, height_left)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1





        