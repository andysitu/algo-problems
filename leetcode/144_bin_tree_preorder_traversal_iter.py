# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        output = []

        q = []
        q.append(root)

        while q:
            n = q.pop()
            
            while n:
                output.append(n.val)
                if n.right:
                    q.append(n.right)
                n = n.left
            
        return output