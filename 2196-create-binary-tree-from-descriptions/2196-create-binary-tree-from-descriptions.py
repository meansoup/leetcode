# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        parents = set()
        childs = set()
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            parent_node = nodes[parent]
            
            if child not in nodes:
                nodes[child] = TreeNode(child)
            child_node = nodes[child]
            
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
                
            parents.add(parent)
            childs.add(child)
        
        root = parents - childs
        
        return nodes[root.pop()]
        
        
        