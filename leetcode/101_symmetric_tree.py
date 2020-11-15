# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            node1 = stack.pop()
            node2 = stack.pop()
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        return True

"""
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
[1,2,2,2,null,2]
"""