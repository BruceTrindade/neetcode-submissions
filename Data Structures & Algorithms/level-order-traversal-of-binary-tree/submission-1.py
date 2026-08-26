# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        tree_layer = []

        queue = deque([root])

        while queue:
            layer_size = len(queue)
            layer = []

            for _ in range(layer_size):
                node = queue.popleft()
                layer.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            tree_layer.append(layer)

        return tree_layer            
