# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equivalent(p, q):
            return (not p and not q) or \
                   (p and q and p.val == q.val)

        def is_same_tree(p, q):
            p_stack, q_stack = [p], [q]
            while p_stack and q_stack:
                p_node, q_node = p_stack.pop(), q_stack.pop()
                if not is_equivalent(p_node, q_node):
                    return False
                
                if p_node:
                    p_stack.append(p_node.left)
                    p_stack.append(p_node.right)
                
                if q_node:
                    q_stack.append(q_node.left)
                    q_stack.append(q_node.right)
            
            return len(p_stack) == len(q_stack)


        stack = [root]
        while stack:
            node = stack.pop()
            if is_same_tree(node, subRoot):
                return True
            
            if node:
                stack.append(node.left)
                stack.append(node.right)
            
        return False