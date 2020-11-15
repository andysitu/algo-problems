# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val > l2.val:
            cur_node = head_node = l2
            curl1 = l1
            curl2 = l2.next
        else:
            cur_node = head_node = l1
            curl1 = l1.next
            curl2 = l2

        while curl1 != None or curl2 != None:
            if curl1 == None:
                cur_node.next = curl2
                cur_node = curl2
                curl2 = curl2.next
            elif curl2 == None:
                cur_node.next = curl1
                cur_node = curl1
                curl1 = curl1.next
            else:
                if curl1.val > curl2.val:
                    cur_node.next = curl2
                    cur_node = curl2
                    curl2 = curl2.next
                else:
                    cur_node.next = curl1
                    cur_node = curl1
                    curl1 = curl1.next
        cur_node.next = None
        return head_node