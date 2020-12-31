class Solution:
    def fib(self, n: int) -> int:
        a, b, c = 0, 1, 0
        for i in range(n):
            b, a = b + a, b
        return a