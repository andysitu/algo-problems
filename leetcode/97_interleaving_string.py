from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def check(self, s1, i, s2, j, s3, k):
        s1len = len(s1)
        s2len = len(s2)
        s3len = len(s3)
        if k >= s3len:
            return True
        elif i >= s1len:
            if s2[j] == s3[k]:
                return self.check(s1,i,s2,j+1,s3,k+1)
            else:
                return False
        elif j >= s2len:
            if s1[i] == s3[k]:
                return self.check(s1,i+1,s2,j,s3,k+1)
            else:
                return False
        else:
            if s1[i] == s3[k] and s2[j] == s3[k]:
                r = self.check(s1,i+1,s2,j,s3,k+1)
                if r == True:
                    return True
                return self.check(s1,i,s2,j+1,s3,k+1)
            elif s1[i] == s3[k]:
                return self.check(s1,i+1,s2,j,s3,k+1)
            elif s2[j] == s3[k]:
                return self.check(s1,i,s2,j+1,s3,k+1)
            else:
                return False

        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)
        s3len = len(s3)
        if s1len + s2len != s3len:
            return False

        result = self.check(s1, 0, s2, 0, s3, 0)
        self.check.cache_clear()
        return result

s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))