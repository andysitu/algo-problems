# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count(self, node, index, k):
        if self.value != None:
            return k+1
        
        if node.left == None:
            if index == None:
                index = 1
            else:
                index = index
        else:
            index = self.count(node.left, index, k) +1

        if index == k:
            self.value = node.val
            return k+1

        if node.right:
            index = self.count(node.right, index+1, k)
        return index
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.value = None
        self.count(root, None, k)
        return self.value