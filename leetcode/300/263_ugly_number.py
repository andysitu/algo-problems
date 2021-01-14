class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        n = num
        while n > 1:
            if n % 2==0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return True