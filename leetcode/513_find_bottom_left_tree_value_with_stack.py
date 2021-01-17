# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return root
        maxLevel = 0
        maxValue = 0
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            if not (node.left or node.right) and level > maxLevel:
                maxValue = node.val
                maxLevel = level
                continue
            if node.right:
                stack.append((node.right, level+1))
            if node.left:
                stack.append((node.left, level+1))
            
        return maxValue