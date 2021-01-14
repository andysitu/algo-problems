class Solution:
    def Match(self, s, p):
        ls = len(s)
        lp = len(p)
        if ls <= 0 and lp <= 0:
            return True
        elif ls > 0 and lp > 0:
            firstp = p[0]
            firsts = s[0]
            if len(p) >= 2:
                sec_p = p[1]
            else:
                sec_p = None

            if firstp == "." and sec_p == '*':
                sa = self.Match(s[1:], p)
                if sa == True:
                    return True
                return self.Match(s, p[2:])
            elif firstp == '.':
                return self.Match(s[1:], p[1:])
            elif sec_p == "*":
                if firsts == firstp:
                    sa = self.Match(s[1:], p)
                    if sa == True:
                        return True
                    return self.Match(s, p[2:])
                else:
                    return self.Match(s, p[2:])
            else:
                if firsts == firstp:
                    return self.Match(s[1:], p[1:])
                else:
                    return False
        elif ls > 0 and lp <= 0:
            return False
        elif ls <=0 and lp >= 0:
            if len(p) >= 2:
                sec_p = p[1]
            else:
                sec_p = None

            if  sec_p == '*':
                return self.Match(s, p[2:])
            return False

    def isMatch(self, s: str, p: str) -> bool:
        status = self.Match(s,p)
        return status
                    
s = Solution()
print(1, s.isMatch("bbbba", "bbbba")==True)
print(2, s.isMatch("bbbba", "bbba")==False)
print(3, s.isMatch("aab", "c*a*b")==True)
print(4, s.isMatch("bbbba", ".*a*a")==True)
print(5, s.isMatch("ab", ".*c")==False) 
print(6, s.isMatch("mississippi", "mis*is*p*.")==False)
print(7, s.isMatch("ab", ".*")==True) 
print(8, s.isMatch("mississippi", "mis*is*ip*.")==True)
print(9, s.isMatch("a", ".*..a*")==False)
print(10, s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b")==True)
print(10, s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b*c*d*e*.*g*b")==True)