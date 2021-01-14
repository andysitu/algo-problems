# never ending loop since b can go on forever
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a & b)
            a = a ^ b
            b = (carry) << 1
        return a


s = Solution()
print(s.getSum())