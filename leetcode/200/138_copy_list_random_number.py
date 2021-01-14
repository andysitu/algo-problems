"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        new_head = Node(head.val)
        node = head.next
        
        prev_n = new_head
        d = {head: new_head}
        
        while(node):
            n = Node(node.val)
            d[node] = n
            prev_n.next = n
    
            prev_n = n
            node = node.next
        
        node = head
        while(node):
            new_node = d[node]
            if node.random:
                new_node.random = d[node.random]
            node = node.next
        return new_head