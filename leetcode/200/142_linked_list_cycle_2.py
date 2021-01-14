# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        forward1 = head
        forward2 = head

        cyclenode = None

        while True:
            forward2 = forward2.next
            if forward2 == None:
                return None
            forward2 = forward2.next
            if forward2 == None:
                return None
            
            forward1 = forward1.next
            if forward1 == forward2:
                cyclenode = forward1
                break

        forward1 = head
        while forward1 != forward2:
            forward1 = forward1.next
            forward2 = forward2.next
        return forward1

def create_cycle(values, loop_index):
    start = ListNode(values[0])
    if len(values) == 1:
        return start
    prev = start

    looped = None
    if loop_index == 0:
        looped = start

    for i in range(1, len(values)):
        n = ListNode(values[i])
        if loop_index == i:
            looped = n
        prev.next = n
        prev = n
    end = n
    if loop_index >= 0:
        end.next = looped
    return start
    
s = Solution()

print(s.detectCycle(create_cycle([3,2,0,-4],1)).val, 2)
print(s.detectCycle(create_cycle([3,2,0,-4],-1)), None)
print(s.detectCycle(create_cycle([3],-1)), None)
print(s.detectCycle(create_cycle([3,2,0,-4],2)).val, 0)
print(s.detectCycle(create_cycle([3,2,0,-4],3)).val, -4)
print(s.detectCycle(create_cycle([3,2,1,22,3,4,5,6,7,3,10,4,3,50,-4],3)).val, 22)
print(s.detectCycle(create_cycle([3,2,1,22,3,4,5,6,7,3,10,4,3,50,-4],0)).val, 3)
print(s.detectCycle(create_cycle([3,2,1,22,3,4,5,6,7,3,10,4,3,50,-4],0)).val, 3)