class Solution:
    def shortestPalindrome(self, s: str) -> str:
        slen = len(s)
        lps = [0] * slen

        i,j=1,0
        while i < slen:
            if s[i] == s[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1

        reverse_s = s[::-1]
        # print(lps)
        
        i, j = 0,0

        while i <= slen-1:
            if reverse_s[i] == s[j]:
                j += 1
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
            
        return reverse_s + s[j:]
        
s = Solution()
print(s.shortestPalindrome("aacecaaa"))
print(s.shortestPalindrome("cacacabc"))
print(s.shortestPalindrome("aaaabaaaaa"))