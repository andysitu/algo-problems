# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def travel(self, node, node2):
        if node == None and node2 == None:
            return True
        elif node == None or node2 == None:
            return False
        
        r = self.travel(node.left, node2.left)
        if r == False:
            return False
        if node.val != node2.val:
            return False
        r = self.travel(node.right, node2.right)
        if r == False:
            return False
        return True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        r = self.travel(p, q)
        if r == False:
            return False
        return True