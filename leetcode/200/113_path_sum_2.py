# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    found_paths = []

    def find_path(self, node, total, sum, paths):
        p = paths + [node.val,]
        
        if node.left is None and node.right is None:
            if node.val + total == sum:
                self.found_paths.append(p)
                return True
            else:
                return False
        else:
            if node.left is not None:
                self.find_path(node.left, node.val + total, sum, p)
            if node.right is not None:
                self.find_path(node.right, node.val + total, sum, p)


    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        self.found_paths.clear()
        self.find_path(root, 0, sum, [])

        return self.found_paths