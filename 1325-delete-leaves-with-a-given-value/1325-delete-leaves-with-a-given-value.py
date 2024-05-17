# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def dfs(self, current: TreeNode, target: int):
         if current.left != None:
             current.left = self.dfs(current.left, target)
         if current.right != None:
             current.right = self.dfs(current.right, target)
        
         print(current.val, current.left, current.right)
        
         if current.left == None and current.right == None and current.val == target:
             return None
         return TreeNode(current.val, current.left, current.right)
 
     def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.dfs(root, target)