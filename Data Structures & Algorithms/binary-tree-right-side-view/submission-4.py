# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        right_nodes = []

        queue = deque([root])

        while queue:
            queue_size = len(queue)

            for item in range(queue_size):
                node = queue.popleft()
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)    
                    
                if item == 0:
                    right_nodes.append(node.val)

        return right_nodes            
