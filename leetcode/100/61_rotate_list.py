# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head == None:
            return head
        n = head
        nodes = []
        while n != None:
            nodes.append(n)
            n = n.next
        nlen = len(nodes)
        
        if k > nlen:
            k %= nlen
        if k == 0 or k == nlen:
            return head
        new_head_i = nlen - k
        new_head = nodes[new_head_i]
        new_tail = nodes[new_head_i - 1]

        # connect the first and lost node
        nodes[nlen-1].next = nodes[0]
        # disconnet head and tail
        new_tail.next = None
        return new_head