from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nlen = len(digits)

        add_status = True
        for i in range(nlen):
            index = nlen - 1 - i
            digits[index] += 1
            d = digits[index]
            if d >= 10:
                digits[index] -= 10
            else:
                add_status = False
                break
        if add_status:
            digits.insert(0, 1)
        return digits

s = Solution()
print(s.plusOne([4,3,2,1]))
print(s.plusOne([4,3,2,9]))
print(s.plusOne([4,3,9,9]))
print(s.plusOne([9,9,9,9,9,9,9,9]))
print(s.plusOne([0]))
print(s.plusOne([1]))
print(s.plusOne([1,1,1,1,1,1,1,1]))