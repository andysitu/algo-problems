"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.
"""

"""
Queue
I beleive you have to explore all the nodes. One way to do that
is to use a queue to do a BFS approach.
Runtime O(n) ; Space O(n)
"""

"""
Recursion / Function Call
Call a new function if there is a left/ right child and have the
parameter contain the current level as well. Then, each function
will either return it's current level if it has no children or th
max level of the results from its children.

Runtime O(n) ; Space O(n) or O(1) depending on how recursion space is viewed
"""
class Solution:
    def explore(self, node, level):
        if not node.left and not node.right:
            return level + 1
        elif not node.left:
            return self.explore(node.right, level+1)
        elif not node.right:
            return self.explore(node.left, level+1)
        else:
            return max(self.explore(node.left, level+1), self.explore(node.right, level+1))
        
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.explore(root, 0)