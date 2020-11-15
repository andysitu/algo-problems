# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxvalue = None
    def pathsum(self, node):
        value = node.val
        left_max_value = None
        right_max_value = None

        lvalue = None
        rvalue = None

        if node.left:
            left_max_value = self.pathsum(node.left)
            lvalue = max(value, left_max_value + value)
        if node.right:
            right_max_value = self.pathsum(node.right)
            rvalue = max(value, right_max_value + value)
        
        if node.left:
            value = max(value, left_max_value + value)
        if node.right:
            value = max(value, right_max_value + value)
        
        self.maxvalue = max(self.maxvalue, value)
        if node.left and node.right:
            return max(lvalue, rvalue)
        elif node.left:
            return lvalue
        elif node.right:
            return rvalue
        else:
            return value
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxvalue = root.val

        self.pathsum(root)

        return self.maxvalue

"""

[5,4,8,11,null,13,4,7,2,null,null,null,1]
"""