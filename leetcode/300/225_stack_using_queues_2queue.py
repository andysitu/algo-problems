import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.cur = 1

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.cur == 1:
            self.q2.put(x)
            while not self.q1.empty():
                self.q2.put(self.q1.get())
            self.cur = 2
        else:
            self.q1.put(x)
            while not self.q2.empty():
                self.q1.put(self.q2.get())
            self.cur = 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.cur == 1:
            return self.q1.get()
        else:
            return self.q2.get()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.cur == 1:
            a= self.q1.get()
            self.q2.put(a)
            while not self.q1.empty():
                self.q2.put(self.q1.get())
            self.cur = 2
        else:
            a= self.q2.get()
            self.q1.put(a)
            while not self.q2.empty():
                self.q1.put(self.q2.get())
            self.cur = 1
        return a

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.cur == 1:
            return self.q1.empty()
        else:
            return self.q2.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()