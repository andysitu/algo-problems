# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        forward1 = head
        forward2 = head

        while True:
            forward2 = forward2.next
            if forward2 == None:
                return False
            forward2 = forward2.next
            if forward2 == None:
                return False
            
            forward1 = forward1.next
            if forward1 == forward2: