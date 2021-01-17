# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return root
        self.max_level = 0
        self.max_value = 0
        
        def travel(node, level):
            if not (node.left or node.right) and level > self.max_level:
                self.max_value = node.val
                self.max_level = level
                return
            if node.left:
                travel(node.left, level+1)
            if node.right:
                travel(node.right, level+1)
        travel(root, 1)
        return self.max_value