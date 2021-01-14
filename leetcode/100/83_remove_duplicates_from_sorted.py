# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        prev_node = head
        node = head.next

        while node:
            if node.val == prev_node.val:
                prev_node.next = node.next
                node = node.next
            else:
                prev_node = node
                node = node.next
            
        return head

s = Solution()