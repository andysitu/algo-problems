from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        abcs = "abcdefghijklmnopqrstuvwxyz"
        wlen = len(words)

        sets = [None] * wlen
        for i in range(wlen):
            sets[i] = set(words[i])

        bitslist = []
        for i in range(wlen):
            b = ['0'] * 26
            for index, c in enumerate(abcs):
                if c in sets[i]:
                    b[index] = '1'
            bitslist.append(int("".join(b), 2))
        
        maxlen = 0
        for i in range(wlen):
            for j in range(i+1, wlen):
                if bitslist[i] & bitslist[j] == 0:
                    maxlen = max(maxlen, len(words[i]) * len(words[j]))
        return maxlen

s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef", "w"]))