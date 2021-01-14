import math

class Solution:
    def convertToTitle(self, n: int) -> str:
        ncount = n
        lstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        letters = ""
        while ncount > 0:
            r = ncount % 26
            if r == 0:
                r = 26
            letters = lstr[r-1] + letters
            ncount = int((ncount - r)/ 26)
        return letters

s = Solution()
print(s.convertToTitle(26))