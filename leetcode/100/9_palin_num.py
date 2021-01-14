class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r = s[::-1]
        len_s = len(s)
        for i in range(len_s):
            if s[i] != r[i]:
                return False
        return True
                    
s = Solution()
print(s.isPalindrome("10001"))
