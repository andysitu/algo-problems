from typing import List
import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
            
class Solution:
    preorder = None
    inorder = None
    inorder_map = None

    def create_tree(self, preorder_index, inorder_start_index, inorder_end_index):

        # print("index", preorder_index, inorder_start_index, inorder_end_index)

        num = self.preorder[preorder_index]

        node = TreeNode(num)
        # print(num)

        if inorder_start_index == inorder_end_index:
            return node

        # find index in inorder or root
        root_inorder_index = self.inorder_map[num]

        num_left = root_inorder_index -  inorder_start_index
        num_right = inorder_end_index - root_inorder_index

        if num_left > 0:
            node.left = self.create_tree(preorder_index + 1, inorder_start_index, inorder_start_index + num_left - 1)
        
        if num_right > 0:
            node.right = self.create_tree(preorder_index + num_left + 1, root_inorder_index + 1, root_inorder_index + num_right)

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.inorder = inorder
        self.preorder = preorder

        self.inorder_map = {}

        for i in range(len(inorder)):
            self.inorder_map[inorder[i]] = i

        nlen = len(preorder)
        if nlen == 0:
            return None
        
        return self.create_tree(0, 0, nlen-1)
        
s = Solution()
s.buildTree([3,9,20,15,7], [9,3,15,20,7])

"""
[3,9,20,15,7]
[9,3,15,20,7]
"""