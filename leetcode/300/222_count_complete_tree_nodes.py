# to solve with the complete tree in mind, my guess is to
# use dfs and search right side first to get the length of the tree and find the last node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count(self, node):
        if node != None:
            self.c += 1
            if node.left:
                self.count(node.left)
            if node.right:
                self.count(node.right)
        
    def countNodes(self, root: TreeNode) -> int:
        self.c = 0
        if root != None:
            self.count(root)
        return self.c
        