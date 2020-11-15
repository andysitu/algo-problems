from typing import List
from functools import cmp_to_key


def compare(a, b):
    return int(a + b) - int(b + a)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numstrs = []
        maxlen = 0
        for n in nums:
            maxlen = max(maxlen, len(str(n)))
            numstrs.append(str(n))
        numstrs = sorted(numstrs, key=cmp_to_key(compare))
        s = ""
        for nstr in numstrs:
            s = nstr + s
        if s[0] == '0':
            return '0'
        return s

s = Solution()
print(s.largestNumber(
[3]))