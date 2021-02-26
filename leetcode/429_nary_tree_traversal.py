"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        l = []
        
        def travel(node, level):
            if (len(l) < level):
                l.append([])
            l[level - 1].append(node.val)
            if node.children:
                for n in node.children:
                    travel(n, level+1)
        if root:
            travel(root, 1)
        return l