# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_max(self, node):
        v = node.val
        
        vl = 0
        under_vl=0
        if node.left:
            vl = node.left.val
            if node.left.left:
                under_vl += node.left.left.val
            if node.left.right:
                under_vl += node.left.right.val
        
        vr = 0
        under_vr=0
        if node.right:
            vr = node.right.val
            if node.right.left:
                under_vr += node.right.left.val
            if node.right.right:
                under_vr += node.right.right.val
        return max(node.val, vl+vr, vl+under_vr, vr+under_vl)
    
    def robbing(self, node):
        if not node.left and not node.right:
            return
        if node.left:
            self.robbing(node.left)
        if node.right:
            self.robbing(node.right)
            
        vl = 0
        if node.left:
            nl = node.left
            if nl.left:
                vl += self.get_max(nl.left)
            if nl.right:
                vl += self.get_max(nl.right)
        vr = 0
        if node.right:
            nr = node.right
            if nr.left:
                vr += self.get_max(nr.left)
            if nr.right:
                vr += self.get_max(nr.right)

        node.val = node.val + vr + vl
        
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        hh = TreeNode(0, root)
        self.robbing(hh)
        
        return max(hh.val, root.val)