from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def travel(self, node, output):
        if node == None:
            return False
        
        self.travel(node.left, output)
        output.append(node.val)
        self.travel(node.right, output)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        self.travel(root, output)
        return output