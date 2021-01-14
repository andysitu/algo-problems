"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None

        stack = []


        visited = [0] * (10 + 1)

        stack.append(node)
        visited[node.val] = 1

        while stack:
            cur_node = stack.pop()

            new_node = Node(cur_node.val)
            visited[cur_node.val] = (cur_node, new_node)

            if cur_node.neighbors:
                for n in cur_node.neighbors:
                    if n.val+1 > len(visited):
                        old_len = len(visited)
                        for i in range(n.val + 10 - old_len):
                            visited.append(0)

                    if visited[n.val] == 0:
                        stack.append(n)
                        visited[n.val] = 1
        
        for ntup in visited:
            if type(ntup) == int:
                continue
            old_n, new_n = ntup[0], ntup[1]
            if old_n.neighbors:
                new_n.neighbors = []
                for nn in old_n.neighbors:
                    new_n.neighbors.append( visited[nn.val][1] )

        return visited[1][1]