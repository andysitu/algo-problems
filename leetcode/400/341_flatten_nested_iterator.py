# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single in  teger that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nlist = nestedList
        self.stack = []
        
        self.curlist = nestedList
        self.index = 0
    
    def next(self) -> int:
        self.index += 1
        return self.curlist[self.index-1]
    
                    
    def hasNext(self) -> bool:
        if not self.stack and not self.curlist:
            return False
        while True:
            if self.index >= len(self.curlist):
                if not self.stack:
                    return False
                c = self.stack.pop()
                self.index = c[1]
                self.curlist = c[0]
            elif self.curlist[self.index].isInteger():
                return True
            else:
                if (self.index+1) < len(self.curlist):
                    self.stack.append((self.curlist, self.index+1))
                self.curlist = self.curlist[self.index].getList()
                self.index = 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())