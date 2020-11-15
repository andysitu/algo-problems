# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, node, length):
        if length == 1:
            return node
        elif length == 2:
            if node.next.val >= node.val:
                return node
            else:
                temp = node.next
                node.next = temp.next
                temp.next = node
                return temp
        else:

            
            l1 = int(length/2)
            l2 = length - l1
            n = node

            for i in range(l1):
                # print(n.val)
                n = n.next

            n1 = self.merge(node, l1)
            n2 = self.merge(n, l2)

            if n1.val <= n2.val:
                start = cur_node = n1
                n1 = n1.next
                l1 -= 1
            else:
                start = cur_node = n2
                n2 = n2.next
                l2 -= 1

            while l1 + l2 > 0:
                if l1 == 0:
                    cur_node.next = n2
                    cur_node = n2
                    n2 = n2.next
                    l2 -= 1
                elif l2 == 0:
                    cur_node.next = n1
                    cur_node = n1
                    n1 = n1.next
                    l1 -= 1
                else:
                    if n1.val <= n2.val:
                        cur_node.next = n1
                        cur_node = n1
                        n1 = n1.next
                        l1 -= 1
                    else:
                        cur_node.next = n2
                        cur_node = n2
                        n2 = n2.next
                        l2 -= 1
                cur_node.next = None
            return start

    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        return self.merge(head, count)




        [4,2,1,3,5, 0, 4,2,4,3,5,6,10,42,52,3,4,6,1,24,5,6,3,1,4,0,-1,43,5,6,6,3,1,4,3,40]