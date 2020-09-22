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

    def partition(self, head: ListNode, x: int) -> ListNode:
        lt_node = None
        head_lt = None
        gte_node = None
        head_gte = None

        node = head

        while node!= None:
            if node.val >= x:
                if head_gte != None:
                    gte_node.next = node
                    gte_node = node
                else:
                    head_gte = node
                    gte_node = node
            else:
                if head_lt != None:
                    lt_node.next = node
                    lt_node = node
                else:
                    head_lt = node
                    lt_node = node
            t = node
            node = node.next
            t.next = None
        
        if head_lt:
            head = head_lt
            if head_gte:
                lt_node.next = head_gte
        elif head_gte:
            head = head_gte
        return head

s = Solution()
print(s.process_nodes(s.partition(s.createnodes( [1,4,3,2,5,2] ), 3) ))