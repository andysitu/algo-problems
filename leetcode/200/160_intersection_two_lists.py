# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        a_len = 0 # a to tail
        b_len = 0 # b to tail

        atail = None
        n = headA
        while n != None:
            a_len += 1
            if n.next == None:
                atail = n
            n = n.next
            
        n = headB
        while n != None:
            b_len += 1
            if n.next == None and n != atail:
                return None
            n = n.next

        a, b = headA, headB
        if a_len > b_len:
            for i in range(a_len - b_len):
                a = a.next
        elif b_len > a_len:
            for i in range(b_len - a_len):
                b = b.next

        while a != None and b != None:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None