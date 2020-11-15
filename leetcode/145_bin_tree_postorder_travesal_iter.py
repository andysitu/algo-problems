# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        output = []
        # output.insert(0, root.val)

        q = []
        q.append(root)

        while q:
            n = q.pop()

            while n:
                output.insert(0, n.val)
                if n.left:
                    q.append(n.left)

                n = n.right
                
            
        return output