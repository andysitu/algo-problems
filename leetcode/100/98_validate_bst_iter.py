# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:       
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        n1 = None
        n2 = None

        stack = []
        min_val = float('-inf')

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= min_val:
                if n1 is None:
                    n1 = 
            root = root.right
            min_val = root.val
        return True

"""
[3,1,5,0,2,4,6]
[10,5,15,null,null,6,20]
[1,1]
[]
[5,1,4,null,null,3,6]
[2,1,3]
"""