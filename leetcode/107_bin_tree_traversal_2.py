from typing import List

import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        q = queue.Queue()
        values = [[root.val]]
        q.put((root.left, -2))
        q.put((root.right, -2))

        while not q.empty():
            nodetup = q.get()
            if nodetup[0] is None:
                continue
                
            while len(values) < -1 * nodetup[1]:
                values.insert(0, [])
            values[ nodetup[1] ].append(nodetup[0].val)
            if nodetup[0].left != None:
                q.put( (nodetup[0].left, nodetup[1] - 1) )
            if nodetup[0].right != None:
                q.put( (nodetup[0].right, nodetup[1] - 1) )
        return values  