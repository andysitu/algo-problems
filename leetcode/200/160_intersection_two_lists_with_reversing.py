# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a_len = 0 # a to tail
        b_len = 0 # b to tail
        b2a_len = 0

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
        
        # point tail to a
        n = headA
        prev = None
        while n != None:
            t = n.next
            n.next = prev
            
            prev = n
            n = t
        
        # count nodes from b to a
        n = headB
        while n != None:
            b2a_len += 1
            n = n.next

        node_from_tail = int((a_len+b_len-b2a_len-1)/2)+1
        
        n = atail
        prev = None
        count = 0
        intersecting_link = None
        while n != None:
            count += 1
            if count == node_from_tail:
                intersecting_link = n
            t = n.next
            n.next = prev
            prev = n
            n = t

        return intersecting_link


# Find distances among the three tails, then x + y, y + z, x + y