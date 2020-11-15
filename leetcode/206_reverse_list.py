# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node):
        if node.next:
            n, head = self.reverse(node.next)
            n.next = node
            return node, head
        else:
            return node, node
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        tail, head = self.reverse(head)
        tail.next = None
        return head