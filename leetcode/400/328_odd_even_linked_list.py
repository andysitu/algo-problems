# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        odd_status = True
        n = head
        odd = even = None
        evenhead = head.next
        while n:
            if odd_status:
                if odd:
                    odd.next = n
                odd = n
                odd_status = False
            else:
                odd_status = True
                if even:
                    even.next = n
                even = n
            n = n.next
        if even:
            even.next = None
        odd.next = evenhead
        return head