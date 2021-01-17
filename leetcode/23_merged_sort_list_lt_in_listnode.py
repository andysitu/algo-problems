import queue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        ListNode.__lt__ = lambda x, y: x.val < y.val
            
        q = queue.PriorityQueue()
        for node in lists:
            if node:
                q.put(node)
        if q.empty():
            return None
        start = q.get()
        cur = start
        if start.next:
            q.put(start.next)
        while not q.empty():
            n = q.get()
            cur.next = n
            cur = n
            if n.next:
                q.put(n.next)
        cur.next=None
        return start