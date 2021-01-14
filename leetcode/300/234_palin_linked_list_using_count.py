# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        n = head
        nlen = 0
        tail = None
        while n:
            nlen += 1
            if n.next == None:
                tail = n
            n = n.next
                
        if nlen == 1:
            return True
        if nlen % 2 == 0:
            switchlen = nlen // 2
        else:
            switchlen = (nlen // 2) + 1
        
        n = head
        prev = None
        count = 0
        while n:
            count += 1
            if count >= switchlen+1:
                t = n.next
                n.next = prev
                prev = n
                n = t
            else:
                prev = n
                n = n.next
        
        ntail, nhead = tail, head
        for _ in range(nlen // 2):
            if ntail.val != nhead.val:
                return False
            ntail, nhead = ntail.next, nhead.next
        return True
        