class Solution:
    def calc(self, s, start, end):
        total= None
        n = None
        nstr = ""
        prev_sign = None
        
        def run_calc():
            nonlocal total, n, nstr
            if total == None:
                if len(nstr) != 0:
                    n = int(nstr)
                total = n
            elif prev_sign == '+':
                if len(nstr) != 0:
                    n = int(nstr)
                total += n
            else:
                if len(nstr) != 0:
                    n = int(nstr)
                total -= n
            nstr = ""
                
        
        nset = {'1','2','3','4','5','6','7','8','9','0'}
        
        i = start
        while i <= end:
            if s[i] in nset:
                nstr += s[i]
            elif s[i] == '+' or s[i] == '-':
                run_calc()
                prev_sign = s[i]
            elif s[i] == '(':
                n, i = self.calc(s, i+1, end)
                continue
            else: # )
                run_calc()
                return total, i+1
            i+= 1
        
        # if s[end] != ')':
        run_calc()
        
        return total, end
            
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        return self.calc(s, 0, len(s)-1)[0]
        

s= Solution()
print(s.calculate("1 + 1"),2)
print(s.calculate(" 2-1 + 2 "),3)
print(s.calculate("(1+(4+5+2)-3)+(6+8)"),3)