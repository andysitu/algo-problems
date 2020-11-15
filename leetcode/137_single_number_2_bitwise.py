from typing import List
import sys

class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        bitsbin = [0] * (len(bin(sys.maxsize))-2)
        negbitsbin = [0] * (len(bin(sys.maxsize))-2)

        npositive = 0

        for n in nums:
            binstr = bin(n)
            if n >= 0:
                npositive += 1
               
                for i in range(len(binstr)-1, 1, -1):
                    if binstr[i] == '1':
                        bitsbin[len(binstr) - i - 1] += 1
                
            else:
                for i in range(len(binstr)-1, 2, -1):
                    if binstr[i] == '1':
                        negbitsbin[len(binstr) - i - 1] += 1

        numstr = ""
        if npositive % 3 == 1:
            for n in bitsbin:
                numstr = str(n % 3) + numstr
            return int(numstr, 2)
        else:
            for n in negbitsbin:
                numstr = str(n % 3) + numstr
            return -int(numstr, 2)

s = Solution()
print(s.singleNumber([2,2,2,5,4,4,4]))
print(s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
print(s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2,1,1,1,4,4,4]))