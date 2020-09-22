from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        nodes_stack = []
        output = []

        while True:
            if node is not None:
                nodes_stack.append(node)
                node = node.left
            elif len(nodes_stack) > 0:
                node = nodes_stack.pop()
                output.append(node.val)
                node = node.right
            else:
                break
        return output