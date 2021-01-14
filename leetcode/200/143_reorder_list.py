# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head == None:
            return None
        if head.next == None:
            return head
        slow = fast = head
        prev_slow = None
        while fast != None and fast.next != None:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        prev_slow.next = None

        cur_node = slow
        prev_node = None
        next_node = None

        while cur_node != None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        listnode1 = head
        listnode2 = prev_node

        while(listnode1 != None):
            prev_nextnode1 = listnode1.next
            prev_nextnode2 = listnode2.next
            listnode1.next = listnode2

            if prev_nextnode1 == None:
                break

            listnode2.next = prev_nextnode1
            listnode1 = prev_nextnode1
            listnode2 = prev_nextnode2