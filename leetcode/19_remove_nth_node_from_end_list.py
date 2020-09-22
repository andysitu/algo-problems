# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        if n <= 0:
            return head
        cur_node = head
        list_len = 0
        saved_node = head
        prev_saved_node = head
        # Iterate thru list & save nth node in each iteration
        while cur_node != None:
            list_len += 1
            if list_len > n:
                prev_saved_node = saved_node
                saved_node = saved_node.next
            cur_node = cur_node.next   
        
        # Delete saved_node
        if saved_node == head:
            return head.next
        if n != 1:
            next_node = saved_node.next
            prev_saved_node.next = next_node
        else:
            prev_saved_node.next = None
        del saved_node
        return head
        

s = Solution()