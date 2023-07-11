class Solution:
    def __init__(self):
        self.result = []

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        parent = self.find_parents(root, target)
        ex = None
        current = target
        for distance in reversed(range(k + 1)):
            if current.left == ex:
                current.left = None
            if current.right == ex:
                current.right = None
            self.child_distance(current, distance)
            if current in parent:
                ex = current
                current = parent[current]
            else:
                break

        return self.result


    def child_distance(self, tree: TreeNode, distance: int):
        if distance == 0:
            self.result.append(tree.val)
        else:
            if tree.left:
                self.child_distance(tree.left, distance - 1)
            if tree.right:
                self.child_distance(tree.right, distance - 1)


    def find_parents(self, tree: TreeNode, target: TreeNode):
        visit = set()
        dfs_stack = [tree]
        parent = {}

        while dfs_stack:
            current = dfs_stack.pop()
            if current == target:
                break
            if current.val not in visit:
                visit.add(current.val)
                if current.right:
                    parent[current.right] = current
                    dfs_stack.append(current.right)
                if current.left:
                    parent[current.left] = current
                    dfs_stack.append(current.left)
        return parent