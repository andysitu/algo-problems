class Solution:
    def intToRoman(self, num: int) -> str:
        n = num
        s = ""
        while n > 0:
            if n >= 1000:
                n -= 1000
                s += "M"
            elif n >= 900:
                n -= 900
                s += "CM"
            elif n >= 500:
                n -= 500
                s += "D"
            elif n >= 400:
                n -= 400
                s += "CD"
            elif n >= 100:
                n -= 100
                s += "C"
            elif n >= 90:
                n -= 90
                s+= "XC"
            elif n >= 50:
                n -= 50
                s += "L"
            elif n >= 40:
                n -= 40
                s += "XL"
            elif n >= 10:
                n -= 10
                s += "X"
            elif n >= 9:
                n -= 9
                s += "IX"
            elif n >= 5:
                n -= 5
                s += "V"
            elif n >= 4:
                n -= 4
                s += "IV"
            elif n >= 1:
                n -= 1
                s += "I"

        return s
        
s = Solution()
print(s.intToRoman(3999))