# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node, output):
        if node == None:
            return

        output.append(node.val)
        self.preorder(node.left, output)
        self.preorder(node.right, output)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        self.preorder(root, output)
        return output