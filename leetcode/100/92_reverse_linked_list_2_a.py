# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def process_nodes(self, head):
        node = head
        numstr = ""
        while node != None:
            numstr += str(node.val) + " "
            node = node.next
        print(numstr)

    def createnodes(self, nums):
        if len(nums) == 0:
            return None
        else:
            nlen = len(nums)
            
            head = ListNode(nums[0])
            node = head
            for i in range(1, nlen):
                n = ListNode(nums[i])
                node.next = n
                node = n
            return head


    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        first_link = head

        for i in range(1, m-1):
            first_link = first_link.next

        node = first_link.next
        next_node = node.next

        prev_start = first_link.next
        print("first_link", first_link.val)
        print("prev_start", prev_start.val)

        for i in range(n-m, n):
            t = next_node.next
            next_node.next = node
            node = next_node
            next_node = t
        prev_end = node
        print(prev_end.val)

        if next_node:
            prev_start.next = next_node
        else:
            prev_start.next = None

        if m != 1:
            first_link.next = prev_end
            return head
        else:
            return prev_end

s = Solution()
s.process_nodes(s.reverseBetween(s.createnodes( [1,2,3,4,5] ), 2, 4 ))
s.process_nodes(s.reverseBetween(s.createnodes( [1,2,3,4] ), 2, 4 ))
s.process_nodes(s.reverseBetween(s.createnodes( [1,2,3,4,5] ), 2, 4 ))
s.process_nodes(s.reverseBetween(s.createnodes( [1,2,3,4] ), 1, 4 ))