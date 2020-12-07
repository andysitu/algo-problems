class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1;
        nums, digits = 9, 9
        ans = 10
        while n > 1 and nums > 0:
            digits *= nums
            ans += digits
            nums -= 1
            n -= 1
        return ans