class Solution:
    def bulbSwitch(self, n: int) -> int:
        counter = 1
        increment = 3
        
        nums = 0
        while counter <= n:
            nums += 1
            counter += increment
            increment += 2
        return nums

s = Solution()
print(s.bulbSwitch(26))