# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        n = head
        prev = None
        if head.val == val:
            while n != None:
                if n.val == val and n == head:
                    head = n.next
                    if prev != None:
                        prev.next = n.next
                    n = n.next
                else:
                    break
        n = head
        prev = None
        while n != None:
            if n.val == val:
                if prev != None:
                    prev.next = n.next
                n = n.next
            else:
                prev = n
                n = n.next
        return head