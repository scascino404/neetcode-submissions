# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def equivalent(p_node, q_node):
            return ((not p_node) and (not q_node)) or \
                   (p_node and q_node and p_node.val == q_node.val)

        p_stack, q_stack = [p], [q]
        while p_stack and q_stack:
            p_node, q_node = p_stack.pop(), q_stack.pop()
            if not equivalent(p_node, q_node):
                return False
            
            if p_node:
                p_stack.append(p_node.left)
                p_stack.append(p_node.right)
            
            if q_node:
                q_stack.append(q_node.left)
                q_stack.append(q_node.right)
        
        return len(p_stack) == len(q_stack)