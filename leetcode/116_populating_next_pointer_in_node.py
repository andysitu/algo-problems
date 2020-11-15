import queue

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        q = queue.Queue()
        prev_q = queue.Queue()
        
        prev_q.put(root)

        node = None
        prev_node = None

        while True:
            if prev_q.empty():
                break
            while not prev_q.empty():
                prev_node = node
                node = prev_q.get()
                # print(node.val)
                if prev_node:
                    prev_node.next = node
                    
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            node.next = None
            node = None
            t = prev_q
            prev_q = q
            q = t
        return root