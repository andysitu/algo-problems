# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, node):
        if node != None:
            node.left, node.right = node.right, node.left
            if node.left:
                self.invert(node.left)
            if node.right:
                self.invert(node.right)
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root