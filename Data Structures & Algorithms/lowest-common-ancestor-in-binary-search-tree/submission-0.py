# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = {root: None}
        stack = [root]
        while stack:
            if (node := stack.pop()):
                if node.left:
                    parent[node.left] = node
                if node.right:
                    parent[node.right] = node
                stack.append(node.left)
                stack.append(node.right)
        
        assert p in parent
        assert q in parent

        p_ancestors = set()
        current = p
        while current in parent:
            if current in parent:
                p_ancestors.add(current)
                current = parent[current]

        current = q
        while current in parent:
            if current in p_ancestors:
                return current
            current = parent[current]
        
        assert False # unreachable