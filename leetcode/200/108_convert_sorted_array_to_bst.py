from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def create_node(self, nums, start, end):
        if end == start:
            # print(nums[start])
            return TreeNode(nums[start])

        if end < start or start < 0 or end >= len(nums):
            return None

        index = int((end+start) / 2)
        # print(nums[index], index, start, end)

        node = TreeNode(nums[index])

        if index-1 >= start:
            node.left = self.create_node(nums, start, index-1)
        if end >= index+1:
            node.right = self.create_node(nums, index+1, end)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        return self.create_node(nums, 0, len(nums) - 1)

s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))