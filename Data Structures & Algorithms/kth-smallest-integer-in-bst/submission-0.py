# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, k_numbers, root):
        if not root: 
            return
        self.inorder(k_numbers, root.left)
        k_numbers.append(root.val)
        self.inorder(k_numbers, root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_numbers = []
        k_numbers.append(0)
        self.inorder(k_numbers, root)
        return k_numbers[k]
        