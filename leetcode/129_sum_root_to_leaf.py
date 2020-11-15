# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0
    def find_leaf(self, node, nstr):
        if not node.left and not node.right:
            self.total += int(nstr + str(node.val))
        
        if node.left:
            self.find_leaf(node.left, nstr + str(node.val))
        if node.right:
            self.find_leaf(node.right, nstr + str(node.val))
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.find_leaf(root, "")
        return self.total