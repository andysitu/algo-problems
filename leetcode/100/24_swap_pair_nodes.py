# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return
        cur_node = head
        cur_next = cur_node.next

        if cur_next == None:
            return cur_node
        head = cur_next
        cur_node.next = cur_next.next
        cur_next.next = cur_node

        prev_node = cur_node
        cur_node = cur_node.next
        while cur_node != None and cur_node.next != None:
            cur_next = cur_node.next
            cur_node.next = cur_next.next
            cur_next.next = cur_node
            prev_node.next = cur_next

            prev_node = cur_node
            cur_node = cur_node.next
            
        return head