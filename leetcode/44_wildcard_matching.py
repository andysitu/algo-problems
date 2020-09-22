class Solution:
    dictMap = []
    def match(self, s, p, i, j):
        s_len = len(s)
        p_len = len(p)
        if i >= s_len and j >= p_len:
            return True
        elif i >= s_len and j < p_len and  p[j] == '*':
            return self.match(s,p,i,j+1)
        elif i >= s_len or j >= p_len:
            return False
        # print(i, j)

        if self.dictMap[i][j] == 1:
            return False

        if p[j] == '?' or s[i] == p[j]:
            return self.match(s, p, i+1, j+1)
        elif p[j] == '*':
            # Ignore the *
            result1 = self.match(s,p,i,j+1)
            if result1:
                return True
            # Use the * and continue using it
            result2 = self.match(s,p,i+1,j)
            if result2:
                return True
            # Use the * and then skip over it
            result3 = self.match(s,p,i+1,j+1)
            if result3:
                return True
        self.dictMap[i][j] = 1
        return False
        
    def isMatch(self, s: str, p: str) -> bool:
        self.dictMap.clear()
        for i in range(len(s)):
            a = [0 for i in range(len(p))]
            self.dictMap.append(a)

        return self.match(s, p, 0, 0)


s = Solution()
print(s.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b")==False)
print(s.isMatch("ho", "**ho")==True)
print(s.isMatch("ho", "ho**d")==False)
print(s.isMatch("ho", "ho**")==True)
print(s.isMatch("aab", "aab*")==True)
print(s.isMatch("", "*")==True)
print(s.isMatch("", "")==True)
print(s.isMatch("a", "a?")==False)
print(s.isMatch("acdcb", "a*c?b")==False)
print(s.isMatch("afabecafbae0", "*1")==False)
print(s.isMatch("aa", "a")==False)
print(s.isMatch("aa", "*")==True)
print(s.isMatch("adceb", "*a*b")==True)
print(s.isMatch("acdcb", "a*c?b")==False)
print(s.isMatch("acdcb", "")==False)
print(s.isMatch("acdcb", "a*")==True)
print(s.isMatch("acdcb", "??????")==False)
print(s.isMatch("acdcb", "?????")==True)
print(s.isMatch("abdfasffasfdsafafsfdafffdafsafdsfdsfafasabdfasffasfdsafafsfdaabdfasffasfdsafafsfdafffdafsafdsfdsfafasfsafsaffffdafsafdsfdsfafasfsafsaffsafsaf", "??????*??") == True)