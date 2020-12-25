"""
Given an array of integers, find out whether there are two distinct 
indices i and j in the array such that the absolute difference between 
nums[i] and nums[j] is at most t and the absolute difference between i 
and j is at most k.
"""

"""
The only solution that I could think up
Have a carry variable
Iterate through the nodes until there are no more in a and b
Add a and b with carry. if it exceeds 10, add the addition 10 to the carry
save the remaining sum (-10) to the new node/ existing node
if it doesn't exceed 10, set carry to 0

add end, if  there is still a carry, attach a node with value 1

return the nodes
"""

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    start = cur = l1
    while l1 or l2:
        if not l2:
            l1.value += carry
            carry = 1 if l1.value >= 10 else 0
            if l1.value >= 10:
                l1.value -= 10
            cur.next = l1
        elif not l1:
            l2.value += carry
            carry = 1 if l2.value >= 10 else 0
            if l2.value >= 10:
                l2.value -= 10
            cur.next = l2
        else:
            s = l2.value + l1.value
            carry = 1 if s >= 10 else 0
            if s >= 10:
                s -= 10
            l1.value = s
            cur.next = l1
    if carry:
        cur.next = ListNode(1)
    else:
        cur.next = None
    return start
    
        