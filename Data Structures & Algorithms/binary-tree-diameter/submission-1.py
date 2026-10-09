# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        max_diameter = 0
        stack = [root]
        while stack:
            if (node := stack.pop()):
                diameter = height(node.left) + height(node.right)
                max_diameter = max(max_diameter, diameter)
                stack.append(node.left)
                stack.append(node.right)
        
        return max_diameter