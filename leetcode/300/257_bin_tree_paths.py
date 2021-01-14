# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travel(self, node, s):
        new_s = s + "->" + str(node.val)
        if not node.left and not node.right:
            self.answer.append(new_s)
            return
        if node.left:
            self.travel(node.left, new_s)
        if node.right:
            self.travel(node.right, new_s)
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if root == None:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        self.answer = []
        if root.left:
            self.travel(root.left, str(root.val))
        if root.right:
            self.travel(root.right, str(root.val))
        return self.answer