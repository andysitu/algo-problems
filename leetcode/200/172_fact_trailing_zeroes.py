class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = n
        count = 0
        while num > 0:
            count += num // 5
            num = num // 5
        return count