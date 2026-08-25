# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, k_numbers, root, k):
        if not root: 
            return
        if len(k_numbers) == k:
            return

        self.inorder(k_numbers, root.left, k)
        k_numbers.append(root.val)
        self.inorder(k_numbers, root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_numbers = []
        self.inorder(k_numbers, root, k)
        return k_numbers[k-1]
        