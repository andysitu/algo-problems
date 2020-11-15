# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isvalid(self, node):
        if node.left is None and node.right is None:
            return True, node.val, node.val
            
        new_max = node.val
        new_min = node.val

        if node.left:
            left_result, left_min, left_max = self.isvalid(node.left)
            if not left_result:
                return False, min(left_min, new_min), max(left_max, new_max)
            if node.val <= left_max or node.val <= node.left.val:
                return False, min(left_min, new_min), max(left_max, new_max)
            
            new_min = min(new_min, left_min)
        if node.right:
            right_result, right_min, right_max = self.isvalid(node.right)
            if not right_result:
                return False, min(right_min, new_min), max(right_max, new_max)
            if node.val >= right_min or node.val >= node.right.val:
                return False, min(right_min, new_min), max(right_max, new_max)
            
            new_max = max(new_max, right_max)
        return True, new_min, new_max
        

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        result, l, r = self.isvalid(root)
        return result

"""
[3,1,5,0,2,4,6]
[10,5,15,null,null,6,20]
[1,1]
[]
[5,1,4,null,null,3,6]
[2,1,3]
"""