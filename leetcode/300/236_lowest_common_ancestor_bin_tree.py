# non-recursive bfs should be faster

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self, node,  v1, v2):
        if self.v != None:
            return 0
        points = 1 if node.val == v1 or node.val == v2 else 0
        if node.left != None:
            points += self.find(node.left, v1, v2)
        if node.right != None:
            points += self.find(node.right, v1, v2)
            
        if points == 2 and self.v == None:
            self.v = node
        return points
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.v = None
        self.find(root, p.val, q.val)
        return self.v