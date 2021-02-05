import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = queue.Queue()
        
        s = 0
        q.put((root, False))
        while not q.empty():
            node, left_status = q.get()
            if node.left or node.right:
                if node.left:
                    q.put((node.left, True))
                if node.right:
                    q.put((node.right, False))
            else:
                if left_status:
                    s += node.val
        return s