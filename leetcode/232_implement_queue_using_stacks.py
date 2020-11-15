# 3 stacks can make it amoritized to O(1) for the push operations by 
# 3rd stack holding he queued values and then finally sorting it out when
# other operations are used

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cur = 1
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.cur == 1:
            curlist, otherlist = self.s1, self.s2 
        else:
            curlist, otherlist = self.s2, self.s1
        while curlist:
            otherlist.append(curlist.pop())
        curlist.append(x)
        while otherlist:
            curlist.append(otherlist.pop())
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s1.pop() if self.cur == 1 else self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[len(self.s1) - 1] if self.cur == 1 else self.s2[len(self.s2) - 1]
            
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0 if self.cur == 1 else len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()