# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    found = False

    def find_path(self, node, total, sum):
        s = node.val + total
        if s > sum:
            return False
        elif self.found:
            return True
        
        if node.left is None and node.right is None:
            if s == sum:
                self.found = True
                return True
            else:
                return False
        else:
            if node.left is not None:
                self.find_path(node.left, s, sum)
            if node.right is not None:
                self.find_path(node.right, s, sum)


    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        self.found = False
        self.find_path(root, 0, sum)

        return self.found