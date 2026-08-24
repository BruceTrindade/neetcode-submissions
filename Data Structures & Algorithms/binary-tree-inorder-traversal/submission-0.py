# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], inorder: List[int]):
        if not root:
            return

        self.dfs(root.left, inorder)
        inorder.append(root.val)
        self.dfs(root.right, inorder)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []

        self.dfs(root, inorder)

        return inorder
        