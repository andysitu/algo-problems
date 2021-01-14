from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return ' ' + str(self.val) + ' '

class Solution:
    def travel(self, node, output):
        if node == None:
            output.append(None)
            return False

        output.append(node.val)
        self.travel(node.left, output)
        self.travel(node.right, output)

    def build(self, i, left, right):
        if left == right:
            return [TreeNode(left),]
        else:
            n = []
            lnodes = []
            rnodes = []
            for l in range(left, i):
                lnodes += self.build(l, left, i-1)
            for r in range(i+1, right+1):
                rnodes += self.build(r, i+1, right)

            if len(lnodes) == 0:
                lnodes.append(None)
            if len(rnodes) == 0:
                rnodes.append(None)

            for lnode in lnodes:
                for rnode in rnodes:
                    node = TreeNode(i, lnode, rnode)
                    n.append(node)
            return n

    def generateTrees(self, n: int) -> List[TreeNode]:

        finalnodes = []

        for i in range(1, n+1):
            nodes = self.build(i, 1, n)
            for node in nodes:
                finalnodes.append(node)

        return finalnodes

s = Solution()
finalnodes = s.generateTrees(3)

for n in finalnodes:
    output = []

    s.travel(n, output)
    print(output)