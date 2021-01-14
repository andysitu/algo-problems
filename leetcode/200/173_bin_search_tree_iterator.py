# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:    

    def __init__(self, root: TreeNode):
        self.nstack = []
        n = root
        while n != None:
            self.nstack.append(n)
            n = n.left
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.nstack.pop()
        if n.right != None:
            ntravel = n.right
            while ntravel != None:
                self.nstack.append(ntravel)
                ntravel = ntravel.left
        return n.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.nstack)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()