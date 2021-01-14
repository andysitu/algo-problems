from typing import List

"""
[3,9,20,null,null,15,7]
[1,2,3,4,null,null,5,1,2,2,3,4,4,3,1,2,2,3,4,4,3,1,2,2,3,4,4,3]
[1,2,3,4,null,null,5]
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
[1,2,2,2,null,2]
"""

import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        q = queue.Queue()
        q.put((root.left, 1))
        q.put((root.right, 1))

        maxlevel = 1

        while not q.empty():
            nodetup = q.get()
            if nodetup[0] is None:
                continue
                
            if nodetup[1]+1 > maxlevel:
                maxlevel = nodetup[1]+1

            if nodetup[0].left != None:
                q.put( (nodetup[0].left, nodetup[1] + 1) )
            if nodetup[0].right != None:
                q.put( (nodetup[0].right, nodetup[1] + 1) )
        return maxlevel