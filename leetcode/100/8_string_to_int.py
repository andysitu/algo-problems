class Solution:
    def is_num(self, ch:str) -> bool:
        letter_value = ord(ch)
        if letter_value >= 48 and letter_value <= 57:
            return True
        return False
        
    def myAtoi(self, s: str) -> int:
        len_s = len(s)
        first_letter = -1
        sign_status = False
        parsed_str = ""
        for i in range(len_s):
            if first_letter == -1:
                if s[i] == "+" or s[i] == "-":
                    if not sign_status and first_letter == -1:
                        parsed_str += s[i]
                        sign_status = True
                    else:
                        return 0
                elif s[i] != " ":
                    if self.is_num(s[i]):
                        first_letter = s[i]
                        parsed_str += s[i]
                    else:
                        return 0
                elif s[i] == " " and sign_status:
                    return 0
            elif self.is_num(s[i]):
                parsed_str += s[i]
            else:
                break
        if len(parsed_str) <= 0:
            return 0
        if sign_status and first_letter == -1:
            return 0
        num = int(parsed_str)
        if num > 2**31-1:
            return 2**31-1
        elif num < -2**31:
            return -2**31
        else:
            return num
                    
s = Solution()
print(s.myAtoi("-91283472332"))

-2147483648