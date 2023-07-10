# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.bfs_queue = []
    
    def minDepth(self, root: Optional[TreeNode]) -> int:        
        if root:
            self.bfs_queue.append((root, 1))
            while True:
                tree, depth = self.bfs_queue.pop(0)
                if tree.left == None and tree.right == None:
                    return depth
                else:
                    if tree.left:
                        self.bfs_queue.append((tree.left, depth + 1))
                    if tree.right:
                        self.bfs_queue.append((tree.right, depth + 1))

        return 0
