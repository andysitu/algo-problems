from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        nodes_stack = []

        prev_val = None
        prev_node = None
        toolarge_node = None
        toosmall_node = None
        afterlarge_node = None

        while True:
            if node is not None:
                nodes_stack.append(node)
                node = node.left
            elif len(nodes_stack) > 0:
                node = nodes_stack.pop()
                if prev_val is not None:
                    if prev_val > node.val:
                        if toolarge_node is None:
                            toolarge_node = prev_node
                            afterlarge_node = node
                        else:
                            toosmall_node = node
                            break
                prev_val = node.val
                prev_node = node
                
                node = node.right
            else:
                break
        if toosmall_node is None:
            toosmall_node = afterlarge_node
        temp_val = toosmall_node.val
        toosmall_node.val = toolarge_node.val
        toolarge_node.val = temp_val

"""
[3,1,4,null,null,2]
[1,3,null,null,2]
"""