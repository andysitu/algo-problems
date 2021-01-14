# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        def robbing(node):
            if not node:
                return (0,0)
            left = robbing(node.left)
            right = robbing(node.right)
            
            robvalue = node.val + left[1] + right[1]
            notrobvalue = max(left) + max(right)
            
            return [robvalue, notrobvalue]
        return max(robbing(root))