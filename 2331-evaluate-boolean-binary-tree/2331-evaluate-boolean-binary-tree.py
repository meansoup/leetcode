# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calc_tree(self, current):
        if current.val < 2:
            return current.val
        if current.val == 2:
            return self.calc_tree(current.left) or self.calc_tree(current.right)
        if current.val == 3:
            return self.calc_tree(current.left) and self.calc_tree(current.right)

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.calc_tree(root)