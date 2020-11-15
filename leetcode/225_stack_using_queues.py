import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = queue.Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        qs = self.q.qsize()
        self.q.put(x)
        for _ in range(qs):
            self.q.put(self.q.get())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.get()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        qs = self.q.qsize()
        a = self.q.get()
        self.q.put(a)
        for _ in range(qs-1):
            self.q.put(self.q.get())
        return a

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()