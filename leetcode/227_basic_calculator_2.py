# Doesn't really need a stack. Can just hold prev num and prev sign

class Solution:
    def calc(self, s):
        def run_calc(n1, n2, sign):
            if sign == '+':
                return n1 + n2
            elif sign == '*':
                return n1 * n2
            elif sign == '/':
                return n1 // n2
            else:
                return n1 - n2
                
        
        nset = {'1','2','3','4','5','6','7','8','9','0'}
        stack = []
        nstr = ""
        n = None
        slen = len(s)
        
        i = 0
        while i < slen:
            if s[i] in nset:
                nstr += s[i]
            else:
                if len(nstr) > 0:
                    n = int(nstr)
                    nstr = ""
                
                if s[i] == '+' or s[i] == '-':
                    while stack:
                        sign = stack.pop()
                        if type(sign) == int:
                            stack.append(sign)
                            break
                        else:
                            n = run_calc(stack.pop(), n, sign)
                    stack.append(n)
                    stack.append(s[i])
                elif s[i] == '/' or s[i] == '*':
                    j = i+1
                    c = s[j]
                    
                    new_str = ""
                    while j < slen and c in nset:
                        new_str += s[j]
                        j += 1
                        if j < slen:
                            c = s[j]
                    next_num = int(new_str)
                    
                    n = run_calc(n, next_num, s[i])
                        
                    i = j - 1
            i += 1
        if len(nstr) > 0:
            n = int(nstr)
            nstr = ""
        while stack:
            sign = stack.pop()
            if type(sign) == int:
                return sign
            else:
                n = run_calc(stack.pop(), n, sign)
        return n

            
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        return self.calc(s)