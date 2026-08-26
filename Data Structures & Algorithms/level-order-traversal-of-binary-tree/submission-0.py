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

        tree_layer = [[]]

        queue = deque([root])
        count = 0

        while queue:
            layer_size = len(queue)

            for _ in range(layer_size):
                node = queue.popleft()
                tree_layer[count].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count += 1
            tree_layer.append([])

        return tree_layer[:-1]            
