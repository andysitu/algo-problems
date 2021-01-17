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
        class CompareNode():
            def __init__(self, node):
                self.node = node
            def __lt__(self, node2):
                return self.node.val < node2.node.val
            
        q = queue.PriorityQueue()
        for node in lists:
            if node:
                q.put(CompareNode(node))
        if q.empty():
            return None
        start = q.get().node
        cur = start
        if start.next:
            q.put(CompareNode(start.next))
        while not q.empty():
            n = q.get().node
            cur.next = n
            cur = n
            if n.next:
                q.put(CompareNode(n.next))
        cur.next=None
        return start