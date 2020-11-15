# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            print(slow.val)
            
        node = None
        while slow:
            tmp = slow.next
            slow.next = node
            node = slow
            slow = tmp
        
        while node:
            if head.val != node.val:
                return False
            node, head = node.next, head.next
        return True