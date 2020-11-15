# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
        nlist = []
        node = head
        while node != None:
            nlist.append(node)
            node = node.next
        
        if len(nlist) % 2 == 1:
            end = int(len(nlist)/2) + 1
        else:
            end = int(len(nlist)/2)

        for i in range(end):
            if i == len(nlist)-i - i:
                nlist[i].next = None
            else:
                nlist[i].next = nlist[len(nlist)-i - 1]
                if i + 1 < end:
                    nlist[len(nlist)-i-1].next = nlist[i+1]
                else:
                    nlist[len(nlist)-i-1].next = None
        return head
