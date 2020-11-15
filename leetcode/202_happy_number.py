class Solution:
    def cycle(self, num):
        s = 0
        while num > 0:
            s += (num % 10)**2
            num = num // 10
        return s
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        fast, slow = n, n
        while True:
            fast = self.cycle(self.cycle(fast))
            slow = self.cycle(slow)
            if fast == 1:
                return True
            if fast == slow:
                return False

s = Solution()

for i in range(1, 20):
    print(i)
    print(s.isHappy(i))