# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, node, output):
        if node == None:
            return

        self.postorder(node.left, output)
        self.postorder(node.right, output)
        output.append(node.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        self.postorder(root, output)
        return output