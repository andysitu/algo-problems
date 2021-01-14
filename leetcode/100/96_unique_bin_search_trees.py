# Note: Can use iterative approach quite easily. It'll be much faster.

from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def build(self, i, left, right):
        if left == right:
            return 1
        else:
            lnodes = 0
            rnodes = 0
            for l in range(left, i):
                lnodes += self.build(l, left, i-1)
            for r in range(i+1, right+1):
                rnodes += self.build(r, i+1, right)

            if lnodes == 0:
                lnodes = 1
            if rnodes == 0:
                rnodes = 1
            
            n = lnodes * rnodes
            return n

    def numTrees(self, n: int):

        finalnodes = 0

        for i in range(1, n+1):
            nodes = self.build(i, 1, n)
            finalnodes += nodes

        return finalnodes

s = Solution()
print(s.numTrees(8))