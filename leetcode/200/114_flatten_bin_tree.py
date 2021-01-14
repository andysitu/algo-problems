# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        stack = []

        prev_node = root
        node = root

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        while stack:
            prev_node = node
            node = stack.pop()

            prev_node.right = node
            prev_node.left = None
            
            if node.right:
                stack.append(node.right)
            
            while node.left:
                prev_node = node
                node = node.left

                prev_node.right = node
                prev_node.left = None

                if node.right:
                    stack.append(node.right)

        return root