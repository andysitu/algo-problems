import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        q = queue.Queue()
        
        output = []
        
        q.put((root, 0))
        while not q.empty():
            t = q.get()
            
            if len(output) == t[1]:
                output.append(t[0].val)
            if t[0].right:
                q.put((t[0].right, t[1]+1))
            if t[0].left:
                q.put((t[0].left, t[1]+1))
        return output
        