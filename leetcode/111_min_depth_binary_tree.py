# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_min_root(self, node):
        if node == None:
            return 0

        left_h = self.get_min_root(node.left)
        right_h = self.get_min_root(node.right)

        if left_h == 0:
            return right_h + 1
        if right_h == 0:
            return left_h + 1
        return min(left_h + 1, right_h + 1)

    def minDepth(self, root: TreeNode) -> int:
        return self.get_min_root(root)

    """
    [1,2,3,4,null,null,5]
    """