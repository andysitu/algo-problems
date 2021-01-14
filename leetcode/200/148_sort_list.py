# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, node):
        if node == None or node.next == None:
            return node

        slownode= node
        fastnode = node
        prev =None

        while fastnode != None and fastnode.next != None:
            prev = slownode
            slownode = slownode.next
            fastnode = fastnode.next.next
        prev.next = None

        n1 = self.merge(node)
        n2 = self.merge(slownode)

        start = ListNode()
        cur_node = start

        while n1 != None and n2 != None:
            if n1.val > n2.val:
                cur_node.next = n2
                n2 = n2.next
            else:
                cur_node.next = n1
                n1 = n1.next
            cur_node = cur_node.next
        if n1 != None:
            cur_node.next = n1
        if n2 != None:
            cur_node.next = n2
            
        return start.next

    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        return self.merge(head)


        [4,2,1,3,5, 0, 4,2,4,3,5,6,10,42,52,3,4,6,1,24,5,6,3,1,4,0,-1,43,5,6,6,3,1,4,3,40]