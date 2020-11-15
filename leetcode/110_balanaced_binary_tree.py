# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_max_height(self, node):
        if node == None:
            return 0
        left_h = self.check_max_height(node.left)
        right_h = self.check_max_height(node.right)

        if left_h == -1 or right_h == -1:
            return -1
        
        if left_h > right_h and left_h - right_h > 1:
            return -1
        else:
            if right_h - left_h > 1:
                return -1
        return max(left_h, right_h) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if self.check_max_height(root) == -1:
            return False
        else:
            return True
        