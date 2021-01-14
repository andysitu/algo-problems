class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False

s = Solution()
print(s.isNumber("0") == True)
print(s.isNumber(" 0.1 ") == True)
print(s.isNumber("abc") == False)
print(s.isNumber("2e10") == True)
print(s.isNumber("-90e03") == True)
print(s.isNumber("--6") == False)
print(s.isNumber("-6") == True)
print(s.isNumber("5.4324abc") == False)
print(s.isNumber("5.4324.") == False)