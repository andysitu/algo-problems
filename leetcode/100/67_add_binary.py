class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        lena = len(a)
        lenb = len(b)
        if lena > lenb:
            biggerlen = lena
            shorterlen = lenb
            bigstr = a
        else:
            biggerlen = lenb
            shorterlen = lena
            bigstr = b

        carry_status = False
        for i in range(shorterlen):
            ai = lena - i - 1
            bi = lenb - i - 1

            if carry_status:
                if a[ai] == '1' and b[bi] == '1':
                    c = '1' + c
                    carry_status = True
                elif a[ai] == '0' and b[bi] == '0':
                    c = '1' + c
                    carry_status = False
                else:
                    c = '0' + c
                    carry_status = True   
            else:
                if a[ai] == '1' and b[bi] == '1':
                    c = '0' + c
                    carry_status = True
                elif a[ai] == '0' and b[bi] == '0':
                    c = '0' + c
                    carry_status = False
                else:
                    c = '1' + c
                    carry_status = False
            # print(c, carry_status, a[i], b[i])
        
        for i in range(shorterlen, biggerlen):
            ii = biggerlen - i - 1
            if carry_status:
                if bigstr[ii] == '1':
                    carry_status = True
                    c = '0' + c
                else:
                    carry_status = False
                    c = '1' + c
            else:
                carry_status = False
                c = bigstr[ii] + c
        
        if carry_status:
            c = '1' + c
        # print(c)
        return c

s = Solution()
print(s.addBinary('11', '1') == "100")
print(s.addBinary('1010', '1011') == "10101")
print(s.addBinary('1010', '1') == "1011")
print(s.addBinary('0', '1') == "1")
print(s.addBinary('0', '0') == "0")
print(s.addBinary('1', '1') == "10")
print(s.addBinary('1', '1') == "10")