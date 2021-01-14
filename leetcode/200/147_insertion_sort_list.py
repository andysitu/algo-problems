# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prev_node = head
        node = head.next
        while node != None:
            # node & prev_node will be used for outer loop iteration
            n = node
            
            if node.val <= head.val:
                prev_node.next = node.next
                node = node.next

                n.next = head
                head = n
            else:
                cur_n = head
                prev_n = None

                while cur_n != None and cur_n.val < n.val:
                    prev_n = cur_n
                    cur_n = cur_n.next
                
                if cur_n == n:
                    prev_node = node
                    node = node.next
                else:
                    prev_node.next = node.next
                    node = node.next
                    
                    prev_n.next = n
                    n.next = cur_n

        return head