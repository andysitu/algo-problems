# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        node = head
        nums = []
        while node != None:
            nums.append(node.val)
            node = node.next
        
        if len(nums) == 0:
            return None
        return self.create_node(nums, 0, len(nums) - 1)

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