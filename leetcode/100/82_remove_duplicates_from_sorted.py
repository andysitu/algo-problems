# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Create a dummy node since head might get deleted
        preNode = ListNode(-1)
        prev_node = preNode
        preNode.next = head

        if head == None:
            return head

        node = head

        while node and node.next:
            if node.val == node.next.val:
                while node and node.next and node.val == node.next.val:
                    node = node.next
                node = node.next
                prev_node.next = node
            else:
                prev_node = prev_node.next
                node = node.next
        return preNode.next

s = Solution()