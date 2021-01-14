import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s).lower()
        slen = len(s)
        if slen % 2 == 0:
            end = int(slen / 2)
        else:
            end = int(slen / 2) + 1
        
        for i in range(end):
            # print(s[i], s[-i], i)
            if s[i] != s[slen-i-1]:
                return False
        return True

s = Solution()
print(s.isPalindrome(" A man, a plan, a canal: Panama "))
print(s.isPalindrome("abcba"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome("abcba"))