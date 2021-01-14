# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        new_lists = [] # Lists that will contain all Nodes w/o linking
        if lists == None or len(lists) <= 0:
            return
        for i in range(len(lists)):
            n = lists[i]
            while n != None and n.val != None:
                new_lists.append(n)
                n = n.next
        if len(new_lists) <= 0:
            return
        new_lists.sort(key=lambda node: node.val)
        first_node = new_lists[0]
        cur_node = first_node
        prev_node = first_node
        for i in range(1, len(new_lists)):
            cur_node = new_lists[i]
            prev_node.next = cur_node
            prev_node = cur_node
        cur_node.next = None
        return first_node
        