class Solution:
    def conv_value(self, c):
        if c == 'I':
            return 1
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        elif c == 'M':
            return 1000
    def romanToInt(self, s: str) -> int:
        l = len(s)
        val = 0
        for i in range(l):
            v1 = self.conv_value(s[i])
            if i + 1< l:
                if v1 < self.conv_value(s[i+1]):
                    val -= v1
                    continue
            val += v1
        return val

s = Solution()
print(s.romanToInt("III"), 3)
print(s.romanToInt("IV"), 4)
print(s.romanToInt("IX"), 9)
print(s.romanToInt("LVIII"), 58)
print(s.romanToInt("MCMXCIV"), 1994)
