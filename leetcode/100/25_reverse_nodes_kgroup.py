# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        nodeslist = []
        cur_node = head
        prev_end = head

        while cur_node != None:
            nodeslist.clear()

            head_node = cur_node
            
            for i in range(k):
                if cur_node == None:
                    break
                nodeslist.append(cur_node)
                cur_node = cur_node.next

            if len(nodeslist) < k: # Not enough nodes for k, leave as is
                if prev_end != head_node:
                    prev_end.next = head_node
            else:
                head_node = nodeslist[0]
                end_node = nodeslist[len(nodeslist)-1]
                
                for i in range(k-1, 0, -1):
                    n = nodeslist[i]
                    prev_n = nodeslist[i-1]
                    n.next = prev_n
                head_node.next = None
                if head_node == head:
                    head = end_node # Set head to start (after reverse)
                else:
                    prev_end.next = end_node # end of last list points to start (after reverse)
                    prev_end = head_node # set marker to end (after rev)
        return head